
from fastapi import FastAPI, Path, Body, Query
import uvicorn
from pydantic import BaseModel, Field, AfterValidator
from typing import Annotated
import random

app = FastAPI()

#               _________________________ QueryParametersStringValidations _________________________

# FastAPI allows you to declare additional information and validation for your parameters.

class Item(BaseModel):
    id: int
    title: str
    Description: str


#               _______________________________ Body Parameter  __________________________________

@app.get("/students")
def MainRoute(items: Annotated[int, Body()]):

    # Item is body Parameter and Annotated gives information to other tools

    # Here Annotated giving info to Fast api to receive item of an integer value and parameter is of body type

    return items


#               ______________________________ Add More Validations  _____________________________

@app.get("/items/")
def read_items_validation(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    results: dict[str, object] = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]
    }

    if q:
        results.update({"q": q})

    return results


#                   __________________________ Add a Regular Expression  ____________________________

@app.get("/item")
def read_items_regex(
    z: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            pattern="^fixedquery$"
        )
    ] = None,
):
    results: dict[str, object] = {
        "item": [
            {"items_id": "Foo"},
            {"items_id": "Bar"}
        ]
    }

    if z:
        results.update({"z": z})

    return results


# This specific regular expression pattern checks that the received parameter value:

# ^: starts with the following characters, doesn't have characters before.

# fixedquery: has the exact value fixedquery.

# $: ends there, doesn't have any more characters after fixedquery.


#               ________________________ Default values ___________________________________

@app.get("/pen/")
def read_pen(
    a: Annotated[str, Query(min_length=3)] = "fixedquery"
):
    results: dict[str, object] = {
        "pen": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }

    if a:
        results.update({"a": a})

    return results


#                   ___________________ Required parameters ________________________

# When we don't need to declare more validations or metadata, we can make the q query parameter required just by not declaring a default value, like:

# q: str

# instead of:

# q: str | None = None

# But we are now declaring it with Query, for example like:

# q: Annotated[str | None, Query(min_length=3)] = None

# So, when you need to declare a value as required while using Query, you can simply not declare a default value:

@app.get("/required-items/")
def read_required_items(
    q: Annotated[
        str,
        Query(min_length=3)
    ],
):
    return {"q": q}


#                       _____________________________ Query parameter list / multiple values ____________________________

@app.get("/multiple-items/")
async def read_multiple_items(
    q: Annotated[list[str] | None, Query()] = None
):
    query_items = {"q": q}
    return query_items


# testing url [http://127.0.0.1:8080/multiple-items/?q=foo&q=bar](http://127.0.0.1:8080/multiple-items/?q=foo\&q=bar)


#                       _______________________________ Additional Validations ____________________________

# alias
# title
# description
# deprecated


#                       ______________________ Alias Parameter __________________________

# Imagine that we want the parameter to be item-query.

# http://127.0.0.1:8000/items/?item-query=foobaritems

# But item-query is not a valid Python variable name

# The closest would be item_query.

# But we still need it to be exactly item-query...

# Then we can declare an alias, and that alias is what will be used to find the parameter value:

@app.get("/items-alias/")
def read_items_alias(
    item_sf: Annotated[
        str | None,
        Query(alias="item-query")
    ] = None
):
    results: dict[str, object] = {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }

    if item_sf:
        results.update({"item_sf": item_sf})

    return results


#                   _________________________ Deprecating parameters  _______________________

# Now let's say we don't like this parameter anymore.

# You have to leave it there a while because there are clients using it, but we want the docs to clearly show it as deprecated.

# Then pass the parameter deprecated=True to Query:

@app.get("/items-deprecated/")
def read_items_deprecated(
    s: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results: dict[str, object] = {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ]
    }

    if s:
        results.update({"s": s})

    return results


#                       ____________________________ Exclude parameters from OpenAPI  ______________________

# To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems), set the parameter include_in_schema of Query to False:

@app.get("/items-hidden/")
def read_hidden_query(
    hidden_query: Annotated[
        str | None,
        Query(include_in_schema=False)
    ] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


#                   ______________________________ Custom Validation ________________________________

import random
from typing import Annotated
from fastapi import FastAPI
from pydantic import AfterValidator
from pydantic import BaseModel

# Create FastAPI application

app = FastAPI()

# Sample data

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


# Custom validation function

def check_valid_id(id: str):

    # Check whether the ID starts with either "isbn-" or "imdb-"

    if not id.startswith(("isbn-", "imdb-")):

        # If the format is invalid, raise a validation error

        raise ValueError(
            'Invalid ID format, it must start with "isbn-" or "imdb-"'
        )

    # If validation is successful, return the ID

    return id


# GET endpoint

@app.get("/books/")
def read_books(

    # id can be a string OR None

    # AfterValidator runs our custom validation function

    # Default value is None, so the parameter is optional

    id: Annotated[
        str | None,
        AfterValidator(check_valid_id)
    ] = None
):

    # If user provides an ID

    if id:

        # Find the book using the given ID

        item = data.get(id)

    # If no ID is provided

    else:

        # Randomly select one ID and its corresponding book

        id, item = random.choice(list(data.items()))

    # Return the ID and book name as JSON

    return {
        "id": id,
        "name": item
    }


#               _________________________ Numeric Validation _______________________________

# And you can also declare numeric validations:

# gt: greater than

# ge: greater than or equal

# lt: less than

# le: less than or equal


#                       ________________________ LE GE  ______________________

@app.get("/students/{id}")
def Route(id: Annotated[int, Path(ge=1, le=100)]):
    return id


#                       ___________________________ LT GT  ______________________

@app.get("/car/{id}")
def source(id: Annotated[int, Path(gt=0, lt=1000)]):
    return id


#                       _____________________________ Body Multiple Parameters ______________________________

# Mix Path, Query and body parameters¶

# First, of course, you can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.

# And you can also declare body parameters as optional, by setting the default to None:

class BodyItem(BaseModel):
    name: str
    description: str | None = None
    price: float


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.get("/items/{item_id}")
def update_item(
    item_id: int,
    item: BodyItem,
    user: User,
    importance: Annotated[int, Body()]
):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance
    }

    return results


#               __________________________  Body - Fields  ______________________________

# When we use a Pydantic BaseModel, it gives us the opportunity to apply custom validations and define validation rules for our data.

# If we are receiving body data through a Pydantic model and we want to apply additional validation rules to individual fields,

# FastAPI/Pydantic provides the Field option for this purpose.

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Field() → allows us to define validation rules and constraints for individual body fields.

class Student(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, lt=100)
    email: str = Field(min_length=5)


#                   ___________________ Temporary data  _____________________________

students: dict[str, Student] = {}


#                    _______________________ POST  _______________________________

@app.post("/students")
def add_student(student: Student):

    # Store student data

    students[student.email] = student

    return {
        "message": "Student added successfully",
        "student": student
    }


#                       _________________ GET _____________________________

@app.get("/students/{email}")
def get_student(email: str):
    student = students.get(email)

    if not student:
        return {
            "message": "Student not found"
        }

    return {
        "student": student
    }


#                       _____________________ PUT  _________________________________

@app.put("/students/{email}")
def update_student(
    email: str,
    student: Student
):

    # Check whether student exists

    if email not in students:
        return {
            "message": "Student not found"
        }

    # Update student data

    students[email] = student

    return {
        "message": "Student updated successfully",
        "student": student
    }


#                       ________________________ Run FastAPI Application   ___________________________

def type():
    uvicorn.run(
        "todos.QueryParametersStringNumValidations:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )

