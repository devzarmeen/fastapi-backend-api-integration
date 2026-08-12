from fastapi import FastAPI, Path, Body, Query
import uvicorn
from sqlmodel import Field , SQLModel, Session, create_engine, select

app = FastAPI()

#           _________ Engine Create _________ 

connection_string = "postgresql://postgres.username:Password@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"
connection  = create_engine(connection_string)
#           _________ Table Create / Schema define  _________
# table will be of name of class
class Students(SQLModel, table = True):
     # Table = true means if table do'snot exist in database we have to create table 
     id : int = Field(default = None , primary_key=True )
     name : str 
     age : int 
     is_active : bool
    
## It will execute the sql model and will create the table on table plus 
SQLModel.metadata.create_all(connection)   
     

##          _____  How to read data ______
@app.get("/getstudents")
def getStudents():
# we will create a session with request to get connected with database connection string 
# after processing we will terminate the session
    with Session(connection) as session:  
        statement = select(Students)  ## Select student table and store in variable statement 
        results = session.exec(statement)  # execute statement
        data = results.all()
        print(data)
        return data

##          ______ Filter Data with Where __________
@app.get("/students")
def getStudentsByName():
    with Session(connection) as session: 
        statement = select(Students).where(Students.name == "zarlish")
        results = session.exec(statement) 
        data = results.all()
        return data      
        
##          _________  Filter Through Client Side __________
# GET a specific student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    with Session(connection) as session:
     # Select student where ID matches
        statement = select(Students).where(Students.id == student_id)
        # Execute statement
        result = session.exec(statement)
        # Get matching record
        student = result.first()
        return student
#      _________________ Run FastAPI Application   ____________________

def type():
  uvicorn.run( "todos.SqlModelDataFetchPostgres:app", host="127.0.0.1", port=8080,reload=True)
 