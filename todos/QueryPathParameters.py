# Client Side Like(Web, Mobile,Postman,Curl)  
 
# Server Side Server app (FastAPI)

## API Receive the data  and API Send Response Data

## Types From which we can sed and receive the data 


from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()
  
  # __________________ Send Data From Client Side __________
@app.get("/")
def MainRoute():
    return "Serve is up and running"

# dynamic route       
@app.get("/students/{id}")
def MainRoute(id):
    return {
       "message" : "Serve is up and running with dynamic route",
       "output" : "id"
       }

# Fix route  with Dynamic Route      
@app.get("/students/{id}/assignments")
def MainRoute(id):
    return {
       "message" : "Serve is up and running with fix route",
       "output" : "id"
       }

# Dynamic route with fix route with dynamic route 
@app.get("/students/{id}/assignments/{assignment_id}")
def MainRoute(id,assignment_id):
    print(id, assignment_id)
    return {
       "message" : "Serve is up and running with dynamic fix dynamic route",
       "output" : "id",
       "assignment_id" : assignment_id
       }
                         
# Query Parameter
#If we try to receive a parameter as input in the API and we have not defined it as a path parameter, the API will consider it a query parameter by default.
@app.get("/students/{id}/assignments/{assignment_id}")
def MainRoute(id,assignment_id,data):  # here data is query parameter
    print(id, assignment_id)
    print(data)
    return {
       "message" : "Serve is up and running with dynamic fix dynamic route",
       "output" : "id",
       "assignment_id" : assignment_id,
       "data" : data
       }

    #To send it using POST, first provide the complete parameter path, then add a question mark (?), followed by the query parameter name used in the function, and assign it a value using = "Value"
    # Example: POST /users?name=Zarlish
    # After question marks path represent to query parameter path and key value should be same as name of parameter in function 
    # for more than 2  or 3 we can use and operator after oe question mark 
    #we might need the parameter to contain /home/zarlish/myfile.txt, with a leading slash (/).
    #In that case, the URL would be: /files//home/zarlish/myfile.txt, with a double slash (//) between files and home.

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
   # return {"file_path": file_path}
   
# Define Types of parameters 
@app.get("/students/{id}/assignments/{assignment_id}")
def MainRoute(id,assignment_id,data:int , username:str, count :int):  # here data is query parameter
    print(id, assignment_id)
    print(data, username, count)
    return {
       "message" : "Serve is up and running with dynamic fix dynamic route",
       "output" : "id",
       "assignment_id" : assignment_id,
       "data" : data,
       "username": username,
       "count": count
       }
## Make Count Optional 
@app.get("/students/{id}/assignments/{assignment_id}")
def MainRoute(id,assignment_id,data:int , username:str, count :int | None = None ):  # here data is query parameter
    print(id, assignment_id)
    print(data, username, count)
    return {
       "message" : "Serve is up and running with dynamic fix dynamic route",
       "output" : "id",
       "assignment_id" : assignment_id,
       "data" : data,
       "username": username,
       "count": count
       }
    
# The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.
        #http://127.0.0.1:8000/items/?skip=0&limit=10
#The query parameters are:
    #skip: with a value of 0
    # limit: with a value of 10
    
# But when we declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

# All the same processes that apply to path parameters also apply to query parameters:

        # Editor support (obviously)
        # Data "parsing"
        # Data validation
        # Automatic documentation
  
# Query parameter type conversion
      
@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# ___________________ Run FastAPI Application ___________________

def type():
    uvicorn.run("todos.QueryPathParameters:app",host="127.0.0.1",port=8080,reload=True)                     