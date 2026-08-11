# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# A request body is data sent by the client to your API. A response body is the data your API sends to the client.
# Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time, 
# sometimes they only request a path, maybe with some query parameters, but don't send a body.
# To declare a request body, you use Pydantic models with all their power and benefits.

from fastapi import FastAPI, Path
import uvicorn
from pydantic import BaseModel


app = FastAPI()


#           _____________ Request Body ______________
#           ____________  Base Model  _____________
        #A parameter for which we define a type-based model is considered required by FastAPI, and FastAPI treats it as a body parameter.
        #If we use a Pydantic model and define its type, even if we pass that type as a parameter in the function, 
        #FastAPI understands that it is a body parameter, not a query parameter.
        # Body parameter is not linked with any url and it is secured
class Item(BaseModel):
    id: int
    title:str
    Description : str 
    # Body Parameter 
@app.get("/students")    
def MainRoute(items: Item):     # Item is body parameter  
    return items
    
#            _____________ Path parameter and Query parameter   ___________
class Items(BaseModel):
    id: int
    title:str
    Description : str 
 
@app.get("/students/{id}/assignments/{assignment_id}")    # {id}/assignments/{assignment_id} are path parameter
def MainRoute(id: int, assignment_id: int, data: int, item: Items):     # data is query parameter and Item is body parameter  
    print(data)
    return item
    return {
       "message": "Serve is up and running with dynamic fix dynamic query route",
       "output": id,
       "assignment_id": assignment_id,
       "data": data,
    }
    # Query will execute by selecting get method from post name using url 
    # http://127.0.0.1:8080/students/72/assignments/13?data=732
   
#           ____________  MAKE BODY PARAMETER OPTIONAL ______________
@app.get("/students/{id}/assignments/{assignment_id}")    # {id}/assignments/{assignment_id} are path parameter
def MainRoute(id: int, assignment_id: int, data: int, item: Item | None = None):     # data is query parameter and Item is body parameter  nad is optional 
    print(data)
    return item 

## How Does FastAPI Identify a Body Parameter?

    # FastAPI determines the type of parameter based on **where it is defined and what type it has**.

### 1. Path Parameter

    # If a variable is defined inside the path using `{}` braces, FastAPI considers it a **Path Parameter**.

    #@app.get("/students/{student_id}")
    #def get_student(student_id: int):

    # {student_id} → Dynamic part of the path
    # /students/ → Fixed part of the path
    # student_id → Path Parameter

### 2. Query Parameter
    # If a parameter is defined in the function with a **simple/singular type** such as:
    # str
    # int
    # float
    # bool

    # FastAPI considers it a **Query Parameter** by default.
    # @app.get("/students")
    # def get_student(name: str, age: int):

    #Here:
    #name: str → Query Parameter
    #age: int → Query Parameter

    # Example request:
    #/students?name=Ali&age=20
    
### 3. Body Parameter

 # If we define a **Pydantic model** using `BaseModel` and use that model as the parameter type in the function, FastAPI considers it a **Body Parameter**.

# from pydantic import BaseModel
# class Student(BaseModel):
    # Name: str
    # age: int
    # @app.post("/students")
    # def add_student(student: Student):

#Here:
    #student: Student
    #is considered a **Body Parameter** because `Student` is a Pydantic `BaseModel`.

    #The data is sent as JSON in the request body:

{
    "name": "Ali",
    "age": 20
}

# **Important:** A parameter does not become a body parameter simply because it has a custom type. It is treated as a body parameter when that type is a **Pydantic `BaseModel`** (under FastAPI's normal parameter inference rules).

#           _______________  Declare it as a parameter _____________

    # To add it to your path operation, declare it the same way you declared path and query parameters:
class Prices(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/prices/")
def create_item(prices: Prices):
    return prices    # declare its type as the model you created, Prices
    
##          _______________  Request body + path parameters _______________

    # You can declare path parameters and request body at the same time.
    # FastAPI will recognize that the function parameters that match path 
    # parameters should be taken from the path, and that function parameters 
    # that are declared to be Pydantic models should be taken from the request body.


class Student(BaseModel):
    name: str
    description: str | None = None
    marks: float
@app.put("/students/{student_id}")
def update_students(students_id: int, students: Student):
    return {"students_id": students_id, **students.model_dump()}

# ___________________ Run FastAPI Application ___________________

def type():
    uvicorn.run("todos.FastApiBodyParameters:app",host="127.0.0.1",port=8080,reload=True)                     