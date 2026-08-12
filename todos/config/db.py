from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv
load_dotenv()
#           _________ Engine Create _________ 

connection_string = os.getenv("DB_URL")
print(connection_string)
engine = create_engine(connection_string)

def create_tables():   
## It will execute the sql model and will create the table on table plus 
    SQLModel.metadata.create_all(engine)
    