# What is an API?

# **API is a function in Python that accepts a request from the frontend, executes the required code/logic inside it, and then sends a response back to the frontend.**
## Main Requirements of a Function

# There are two main requirements:

# 1. **Code / Business Logic**
# 2. **Code to receive the request and send the response**

# **Request and response handling will be managed by FastAPI.**

### REST API

# **A REST API responds with data in JSON format.**

#We will mainly focus on the **business logic**.

# Four Main Pieces of Information Required for Request & Response

   # IP Address
   # Port Number
   # Route of Function
   # API Method (GET, POST, PUT, DELETE)

# ________________________ How Function Sends Response From Backend to Frontend ________________________

from fastapi import FastAPI
import uvicorn

## Variable

app = FastAPI()         # Call the FastAPI function and save it in the app variable
@app.get("/gettodos")   ## app.get() handles the request and response
## "/gettodos" is the route

def getTodos():  # Create Function
    print("Get todos called")
    return "gettodos called"

# The function will be called by @app.get("/gettodos"), and it is handled by FASTAPI

# **FastAPI receives the request from the frontend/client, matches the request with the route, calls the corresponding function, and sends the response back to the frontend.**

## Get Single Todo

@app.get("/getSingleTodo")   ## Route name

def getSingleTodo():
    print("Get SingleTodo Called")
    return "Get Single todo called"

# **In one application, two functions cannot have the same route name with the same API method.**

# **Two devices cannot have the same IP address.**

# **Two applications cannot use the same port number at the same time.**

## Same Route with Different API Methods

# If you want to create the same route for two functions, then the **API method type should be different**.

@app.post("/getSingleTodo")   ## Route names are the same, but the API method type is different

def getSingleTodoPost():
    print("Get Post Method SingleTodo Called")
    return "Post method Single todo called"

# Uvicorn

# **Uvicorn is used to run the Python file/application.**

## Function for Uvicorn

def start():
    uvicorn.run("todos.SendResponse\:app",host="127.0.0.1", port=8080, reload= True)
    
    ## IP address "127.0.0.1" is used for development and testing on the same device.
    ## It is also called localhost.

    ## 0.0.0.0 is also a local host IP address.

    ## Port number can vary, such as 3000 for frontend,
    ## 5000, or any other available port.

    ## "todos.main\:app"
    ## todos is the folder name
    ## main is the file name
    ## app is the variable where the FastAPI application lives

# All Three APIs Can Have the Same Path but Different Methods

# List

@app.post("/")
def List():
    return[1,2,3,4,5]

# Dictionary

@app.put("/")
def dict():
    return{
    "Alisha" : "Zarmeen"
    }
# String 

@app.get("/")
def helloWorld():
    return "Hello, World from 1st Reload!"


# **The server will execute the current function when running `poetry run dev`.**


# Reload Option in Uvicorn

# After adding a new function in the API, normally we have to stop the current server processing and restart the server by running:

            # poetry run dev

# To avoid this interruption, **Uvicorn provides the `reload = True` option.**

    # It means whenever I make changes in the code,
    # the server will automatically reload.
    # Changes will become live without manually restarting the server.

# API Documentation

# To view the documentation of all your APIs, open the browser and enter:
    
    # http://127.0.0.1:8080/docs
#
# **FastAPI automatically generates the API documentation.**

# PUT API for Update

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"

# **PUT API is generally used to update existing data.**


# Main Task of a Backend Function

#  **The main task of a backend function is to receive data from the frontend, process it using the required business logic, and send a response back to the frontend.**