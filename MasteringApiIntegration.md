##          -----------  API -------------

All process of request, response, third party handling, and database handling is also known Application Programming Interface(API)

Communication medium between two applications is API 

## Rest API's:

Some API's send  json format, Structure, object in response  these are rest api's.

# API's

Some Apis send json files (pdf, image ,html, files)   in  response these are normal api's.

## Graph API 
Graph Api may also return json, but structure is different from REST APIs

## Mostly used is REST API'S 

## Json Format

json stores data in key value pairs in curly braces 
{
    "key" : "Value"
    "name : "Alisha"
    "email" : "Zarmeen@gmail.com"
}

# Postman 

Postman is an API development and testing tool that allows developers to send HTTP requests to a backend server without creating a frontend application.

It helps developers test, debug, and document APIs quickly and efficiently.

# Why do ewe use it?

Normally, the communication flow is:

Frontend → Backend → Database

While developing a backend, the frontend may not be ready yet.

Instead of waiting for the frontend, we use Postman to send requests directly to the backend.

This allows us to:

- Test APIs
- Verify responses
- Debug errors
- Check request and response data
- Test authentication
- Save and organize API collections
 
# How Postman Works

Postman
     │
     ▼
HTTP Request
     │
     ▼
Backend API
     │
     ▼
Database
     │
     ▼
Backend API
     │
     ▼
HTTP Response
     │
     ▼
Postman

## HTTP Methods in Postman 

1. GET

Purpose: Retrieve data from the server.

2. POST

Purpose: Create a new resource.

3. PUT

Purpose: Update an entire resource.

4. PATCH

Purpose: Update only specific fields.

5. DELETE

Purpose: Delete a resource.

## Headers

Headers send additional information with the request.

# Body 
used mainly with post put patch 

## Params

Used to send query parameters.

## Common Postman Features

- Send API requests
- Save requests in collections
- Organize APIs into folders
- Store environment variables
- Test authentication (JWT, OAuth, API Keys)
- Upload files
- Generate API documentation
- Write automated API tests
- Import and export API collections

Post has its ow documentation 

The methods in request respose, function and method in postman should be same 

We write documents as a backend developer to share some necessary information with frontend developer

## 1. Postman Documentation

Store documents for backend developers and fronted developers

## 2.Swagger Tool

It is website for storing the documentation about softwares ApI's
**Link** : https://swagger.io/

## 3.Website Documentation 
It contain's complete website for documentation 


## API METHODs

Get, Post, Put, Delete, Patch 

## How Postman url works?

https://api.github.com/users/abc 

1. We have code in our laptop  

2. Shift code to the Server(Server Application)

3. Users communicate with server to access the Resources 

# Servers are of two types 

one we have our own server , and for other one we have pay for . this i called private cloud public cloud and 

- Servers are far away from user that why they are called cloud

# IP Address

- We need the address of server (ip address of an server) 
post man required that ip address to send request and users will access services from that device easily from world wide 

http://192.131.1.1     // computer or server number 

# Port Number 

- There are multiple applications on serever to get acesss on specific application we need to specify the port number 

- One server or one computer can contin alomost 65 thousand ports 

http://192.131.1.1:3000   # :3000 is port number : represent port number 

- Each backend function represents different path 
**GET**  http://192.131.1.1:3000/createuser 

   it indicates that access the 192.131.1.1 computer on port 30000 and the utilize function create user 

   **POST** http://192.131.1.1:3000/adduser

   https://apis.github.com/users/abc    here apis.github is domain that is stored on the central server  users is path / route                           

# EXAMPLE FASTAPI

**LINK**: https://fastapi.tiangolo.com/#example-upgrade
   @app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

    FUNCTION WILL BE USED WHEN PATH will be ("/items/{item_id}")  and method will be get