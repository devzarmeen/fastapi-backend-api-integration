from fastapi import FastAPI, HTTPException, Path, Body, Query
from fastapi.responses import FileResponse
import uvicorn
import csv

from sqlmodel import Session, select
from dotenv import load_dotenv  ## Library to import the env file where we keep our connection string 
# Load .env variables
load_dotenv()

from .config.db import create_tables, engine  # import db file
from .models.todos import Todo    # Import models files
from .models.todos import UpdateTodo  # import updatetodomodel

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
    with Session(engine) as session:   # with helps to handle session create,  close session error handle automatically
        statement = select(Todo)  ## Select student table and store in variable statement 
        results = session.exec(statement)  # execute statement
        data = results.all()
        print(data)
        return data

##          ______  Filter Data with Where ______
@app.get("/get_todo{to_id}")
def gettodosbytitle(todo_id:int):
    with Session(engine) as session: 
        statement = select(Todo).where(Todo.id == todo_id)
        results = session.exec(statement) 
        data = results.all()
        return data

##          ______  Post Data  ______
@app.post("/create_todo")
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"status":200, "message":"todo created successfully"} 
    
##          ______  Put Data  ______

        ## we can create a new model or can use base model as well  
@app.put("/update_todo/{id}")
def update_todo(id:int, todo : UpdateTodo):
    with Session(engine) as session:
        db_todo= session.get(Todo, id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="DbTodo not found")
        todo_data = todo.model_dump(exclude_unset= True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"status":200, "message":"updated todo created successfully"}
    
##          ______  Delete Data  ______
@app.delete("/delete_todo/{todo_id}")
def delete_todo(todo_id:int):
    with Session(engine) as session:
        print(todo_id)
        db_todo= session.get(Todo, todo_id)                     
        if not db_todo:
            raise HTTPException(status_code=404, detail="db_Todo not found")
        session.delete(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"status":200, "message":"todo deleted successfully"}
##          _______  Download CSV File _____
# __________ Download CSV File __________

#@app.get("/download_csv")
#def download_csv():
    # Create database session
    #with Session(engine) as session:
        # Get all Todo records from database
     #   statement = select(Todo)
      #  results = session.exec(statement)
       # todos = results.all()
        # CSV file name
        #file_name = "todos.csv"

        # Create CSV file
        #with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
            # Define CSV columns
         #   fieldnames = ["id", "title", "description", "is_completed"]
            # Create CSV writer
          #  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write column headers
           # writer.writeheader()
            # Write database records
            #for todo in todos:
             #   writer.writerow({
              #      "id": todo.id,
               #     "title": todo.title,
                #    "description": todo.description,
                 #   "is_completed": todo.is_completed
                #})
    # Return CSV file for download
    #return FileResponse(
     #   path=file_name,
      #  filename="todos.csv",
       # media_type="text/csv"
    #)
#      _______ Run FastAPI Application   _________

def type():
    ##  Before Application startup we want to create table then run app 
    create_tables()
    uvicorn.run( "todos.DynamicTodosAppSQLModel:app", host="127.0.0.1", port=8080,reload=True)
 