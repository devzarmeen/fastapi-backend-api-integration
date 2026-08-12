from fastapi import FastAPI, Path, Body, Query
import uvicorn
from sqlmodel import Session, select
from dotenv import load_dotenv  ## Library to import the env file where we keep our connection string 
# Load .env variables
load_dotenv()
from .config.db import create_tables, engine  # import db file
from .models.todos import Todos        # Import models files

# Environment Variables with python-dotenv

# load_dotenv() loads variables from the .env file into the current environment.
# os.getenv() is used to access these variables.
# Example:
# DATABASE_URL=postgresql://username:password@host:5432/db
# os.getenv("DATABASE_URL")

# Access environment variable
#connection_string = os.getenv("DATABASE_URL")
# Install with Poetry:
# poetry add python-dotenv


app = FastAPI() 
 

##          _____  How to read data ______
@app.get("/gettodos")
def gettodos():
# we will create a session with request to get connected with database connection string 
# after processing we will terminate the session
    with Session(engine) as session:  
        statement = select(Todos)  ## Select student table and store in variable statement 
        results = session.exec(statement)  # execute statement
        data = results.all()
        print(data)
        return data

##          ______  Filter Data with Where ______
@app.get("/get_todos")
def gettodosbytitle():
    with Session(engine) as session: 
        statement = select(Todos).where(Todos.title == "zarlish")
        results = session.exec(statement) 
        data = results.all()
        return data

#      _______ Run FastAPI Application   _________

def type():
    ##  Before Application startup we want to create table then run app 
    create_tables()
    uvicorn.run( "todos.DynamicTodosAppSQLModel:app", host="127.0.0.1", port=8080,reload=True)
 