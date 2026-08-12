# ________________________ How Function Receives Request from Frontend to Backend ________________________

# Types of Receiving Request frm Frontend

        # 1. Path Variable / Dynamic path
        # 2. Query Param 
        # 3. Body Json

from fastapi import FastAPI
import uvicorn

## Variable
app1 = FastAPI()  
 
 #              -------------------1. Path Variable  -----------------------
 ## Send and receive the same thing
@app1.get("/gettodos/{id}")         #gettodos is dynamic path and {id} is dynamic path can be received by fronted 
def getTodos(id):  # Create Function and path will also be written in function parameter and it will store that value of sent by frontend
    print("Get todos called By dynamic path",id)
    return id  


## Different fronted nd backend request 
@app1.post("/gettodos/{id}")         #gettodos is dynamic path and {id} is dynamic path can be received by fronted 
def postTodos(id):  # Create Function and path will also be written in function parameter and it will store that value of sent by frontend
    print("post todos called By dynamic path",id)
    return "The fronted request is different and backend response is different"

        # You can only access only  number of variables written in function
        # If you write  one variable you can access only one value 
        # If you  access more than one variable it will give error 
    
## 2 dynamic variables path
@app1.get("/getdos/{rollno}/{username}")
def getTodo(rollno,username):
    print("Get Todos called By dynamic path",rollno,username)
    return rollno + username

##  We call also define type of variables 
@app1.get("/getdos/{rollno}/{username}")
def getTodo(rollno:str,username:str):
    print("Get Todos called By dynamic path",rollno,username)
    return rollno + username


    # Uvicorn

# **Uvicorn is used to run the Python file/application.**

## Function for Uvicorn

def running():
    uvicorn.run("todos.sendrequest:app1",host="127.0.0.1", port=8080, reload= True)
    
    ## IP address "127.0.0.1" is used for development and testing on the same device.
    ## It is also called localhost.

    ## 0.0.0.0 is also a local host IP address.

    ## Port number can vary as 8081, such as 3000 for frontend,
    ## 5000, or any other available port.

    ## "todos.sendrequest\:app1"
    ## todos is the folder name
    ## sendrequest is the file name
    ## app1 is the variable where the FastAPI application lives


    ## http://127.0.0.1:8081/gettodos/13    this link will be used to run function on local host 
        # 13 is value of id 8081 is port number and 127.0.0.1  is local host ip address 



##  ----------------- 2. Query Param  ----------------- 
         # in query param we dont write anything along with path 
@app1.get("/getSingleTodo")
def getSingleTodo(username:str, rollno:str):
    print("Query Param Get todo Called",username , rollno)
    return "Query param getSingleTodo called"
        ## In query param we define the path till 127.0.0.1  and them write the key values 

## Store the data of Student 
students= [{
    "username" : "AlishZari",
    "rollno": "373112"
}]

@app1.get("/students")
def getStudents():
    return students

# ----------------- Add Student  Using Query Param  ------------
@app1.get("/addStudent")
def addStudent(username: str, rollno: str):
    global students
    students.append({"username": username, "rollno": rollno})
    return students

## @ 2 students Data store
students1 = [{
    "username" : "Alisha",
    "rollno": "373"
},
             {
    "username" : "Zarmeen",
    "rollno": "112"             
}
             ]

@app1.get("/students1")
def getStudents():
    return students1


##   ------------------- Delete Student Using Query Param -----------------------

@app1.delete("/deleteStudent") 
def deleteStudent(rollno: str): 
    global students 
    # Loop through all students 
    for student in students:
        # Check if rollno matches 
        if student["rollno"] == rollno: 
            # Remove the student from the list 
            students.remove(student) 
            # Return updated student list 
            return students 
        # If rollno is not found return "Student not found"
        
#   -------------  Update Student Using Query Param --------------
#For updating a student, we need:

    #1. Existing rollno → To find the student
    # 2. New username     → To update username
    # 3. New rollno       → To update roll number  
    
@app1.put("/updateStudent")
def updateStudent( rollno: str, username: str, newrollno: str ):
    global students
    # Loop through all students 
    for student in students: 
    # Find student using existing rollno 
        if student["rollno"] == rollno: 
            # Update username 
            student["username"] = username 
            # Update rollno 
            student["rollno"] = newrollno 
            # Return updated student list 
            return students 
        # If student is not found 
    return "Student not found"

# ------------------- Filter Student By Username and Roll Number ----------------------- 
@app1.get("/filterStudentMultiple") 
def filterStudentMultiple(username: str, rollno: str): 
    # Create an empty list to store filtered students 
    filteredStudents = [] 
    # Loop through all students 
    for student in students: 
    # Check both username and rollno 
        if student["username"] == username and student["rollno"] == rollno: 
            # Add matching student to filtered list 
            filteredStudents.append(student) 
    # Return filtered students 
    return filteredStudents