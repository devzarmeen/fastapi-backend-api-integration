from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


# __________________________ Add Types __________________________

# We use a colon (:) to add a type annotation, not an equals sign (=).
# The equals sign (=) is used to assign a value or set a default value.
# Adding type hints normally does not change how the code behaves at runtime.
# Type hints mainly help with code readability, editor support, and type checking.

username: str = "zarlish"
age: int = 21
height: float = 5.8
is_active: bool = True
data: bytes = b"Hello"


# ___________________ Declaring Simple Types ___________________

# int
# float
# bool
# bytes


# ___________________ 1. Define Parameter Type String ___________________

def getUserFullName(firstname: str, lastname: str):
    return firstname + "" + lastname


# ___________________ 2. Define Parameter Type String plus Integer ___________________

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


# ___________________ 3. Define Parameter Type Float ___________________

def get_user_height(height: float):
    # float receives decimal values.
    return height


# Example

get_user_height(5.8)


# ___________________ 4. Define Parameter Type Boolean ___________________

def check_user_active(is_active: bool):
    # bool parameter will receive either True or False.
    return is_active


# Example

check_user_active(True)


# ___________________ 5. Define Parameter Type Bytes ___________________

# Define Parameter Type Bytes

def get_data(data: bytes):
    # bytes represents binary data.
    return data


# Example

get_data(b"Hello")


# ___________________ Typing Module ___________________

# For some additional use cases, we might need to import
# some things from the standard library typing module.
# For example, when we want to declare that something can have
# any type, we can use Any.

from typing import Any
def some_function(data: Any):
    print(data)


# ___________________ Generic Types ___________________

# Some types can take "type parameters" in square brackets
# to define their internal types.
# These types have internal types called generic types.
#
# We declare the variable using the same colon (:) syntax.
#
# 1. List
# 2. Dictionary
# 3. Set
# 4. Tuple


listitems: list[str] = ["first", "second", "third"]
prices: dict[str, float] = {
    "pen": 12.5,
    "book": 250.0,
    "pencil": 20.0
}


# ___________________ List ___________________

# The variable items is a list,
# and each item in this list is of type str.

from typing import List
def process_items(items: list):
    for item in items:
        print(item)


# ___________________ Tuple and Set ___________________

# The variable item_t is a tuple.
# The variable item_s is a set,
# and each item in this set is of type bytes.
from typing import Tuple
from typing import Set

def process_item(item_t: tuple, item_s: set[bytes]):
    return item_t, item_s


# ___________________ Dict ___________________

# To define a dict, we pass 2 type parameters, separated by a comma.
# The first type parameter is for the keys of the dict.
# The second type parameter is for the values of the dict.

from typing import Dict
def process_prices(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# The variable prices is a dict:

# The keys of this dict are of type str
# (for example, the name of each item).
#
# The values of this dict are of type float
# (for example, the price of each item).


# ___________________ Poetry and Mypy ___________________

# Activate the Poetry environment through the command:
# poetry shell
#
# If we make any changes to pyproject.toml,
# we should install and lock the dependencies again:
#
# poetry install
# poetry lock
#
# Add mypy to the project dependencies using:
#
# poetry add mypy
#
# Run mypy using the following command to check
# whether there are any type-related errors:
#
# mypy todos/pythontypes.py


# ___________________ Union ___________________

# We can declare that a variable can have one of several types.
# For example, it can be either an int or a str.
#
# To define a union using modern Python syntax,
# we use the vertical bar (|) to separate the types.
#
# This is called a "union" because the variable
# can contain a value from any of the specified types.

from typing import Union


# Using Union with multiple types.
# Union[int, str]
# because this is the standard syntax when using typing.Union.

def item_union(item: Union[int, str]):
    print(item)

# The function performs string concatenation,
# so firstname should be a string.
def getname(firstname: str, lastname: str, age: int):
    return firstname + "" + lastname


# This means that item could be an int or a str.


# ___________________ Possibly None ___________________

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# Using str | None instead of just str will let the editor
# help us detect errors where we might assume that a value
# is always a str, when it could actually be None too.


# ___________________ Optional ___________________

from typing import Optional

def say_hlo(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello Zarlish")


# ___________________ Pydantic Models ___________________

# Pydantic is a third-party Python library used for data validation.
#
# We declare the "shape" of the data as classes with attributes.
# Each attribute has a type.
#
# Then we create an instance of that class with some values.
# Pydantic validates the values, converts them to the appropriate
# type when possible, and gives us an object containing the data.

from datetime import datetime
from typing import Any
from pydantic import BaseModel
# BaseModel helps us define types for each property of an object
# and provides data validation and conversion.


class User(BaseModel):
    id: int
    name: str = "zari alish"
    signup_ts: datetime | None = None
    friends: list[int] = []


user_data: dict[str, Any] = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"]
}

user = User(**user_data)

print(user)
# User id=123 name='zari alish'
# signup_ts=datetime.datetime(2017, 6, 1, 12, 22)
# friends=[1, 2, 3]

print(user.id)      # 123


# FastAPI is heavily based on Pydantic for data validation and models.


# ___________________ Example 2 ___________________

class Todo(BaseModel):
    rollno: int
    title: str = "any default title value"
    description: str
    completed: bool = False
    created_at: datetime | None = None
    tags: list[str] = []


# Pydantic can convert the external values at runtime,
# but mypy needs to know that the dictionary can contain values
# of different types.

todo_data: dict[str, Any] = {
    "rollno": "101",
    "description": "Learn FastAPI and Pydantic",
    "completed": "True",
    "created_at": "2026-08-10 18:30",
    "tags": ["FastAPI", "Pydantic", "Python"],
}
todo = Todo(**todo_data)
print(todo)


# ___________________ Metadata Annotations ___________________

# Python itself does not perform any special operation with Annotated.
#
# The important thing to remember is that the first type parameter
# passed to Annotated is the actual type.
#
# The remaining parameters are metadata that can be used by
# other tools and libraries such as FastAPI.

from typing import Annotated
# A default value for an int parameter must also be an int.
# Path(ge=10) means that FastAPI should validate that age
# is greater than or equal to 10.

def hello(age: Annotated[int, Path(ge=10)]) -> str:
    # The first parameter represents the actual type.
    # The remaining parameters represent additional metadata.
    # This metadata does not change the basic Python type itself.
    return f"Hello {age}"


# But we can use this space in Annotated to provide FastAPI
# with additional metadata about how you want your application to behave.
#
# The important thing to remember is that the first type parameter
# you pass to Annotated is the actual type.
# The rest is just metadata.


# ___________________ Type Hints in FastAPI ___________________

# FastAPI takes advantage of these type hints to do several things.
#
# With FastAPI, you declare parameters with type hints and you get:
#
#     Editor support.
#     Type checks.
#
# FastAPI uses the same declarations to:
#
# Define requirements:
#     Request path parameters, query parameters, headers,
#     request bodies, dependencies, etc.
#
# Convert data:
#     Convert data from the request to the required type.
#
# Validate data:
#     Validate data coming from each request.
#
# Generate automatic errors:
#     Return automatic validation errors to the client
#     when the provided data is invalid.
#
# Document the API using OpenAPI:
#     OpenAPI is then used by automatic interactive
#     documentation user interfaces such as Swagger UI.


# ___________________ Run FastAPI Application ___________________

def type():
    uvicorn.run("todos.pythontypesPydanticAnnotated:app",host="127.0.0.1",port=8080,reload=True)