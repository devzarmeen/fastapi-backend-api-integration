from fastapi import FastAPI, Path, Body, Query
import uvicorn
from sqlmodel import Field , SQLModel, Session, select

##       ----------  Model Create --------
class Todo(SQLModel, table = True):                      
     # Table = true means if table do'snot exist in database we have to create table 
     id : int = Field(default = None , primary_key=True )
     title : str  
     description : str 
     is_completed : bool
     
##       ----------  Update Model Create --------
class UpdateTodo(SQLModel):                      
     title : str  | None
     description : str   | None
     is_completed : bool  | None