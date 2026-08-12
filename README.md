# FastAPI Backend API Integration

A professional FastAPI backend project demonstrating REST API development, PostgreSQL database integration, SQLModel ORM, CRUD operations, environment-based configuration, API validation, and API documentation with Swagger UI.

## 🚀 Project Overview

This project is built with **FastAPI** and demonstrates how a backend application communicates with a PostgreSQL database using **SQLModel**.

**The project covers:**

- FastAPI REST APIs
- Path & Query Parameters
- Request Body Handling
- PostgreSQL Integration
- SQLModel ORM
- CRUD Operations
- Environment Variables
- Secure Database Configuration
- CSV Data Export
- API Validation
- Swagger / OpenAPI Documentation
- Poetry Environment Management
- Mypy Type Checking


## 🛠️ Tech Stack

| Technology           | Purpose 

| Python               | Backend Development 

| FastAPI              | REST API Framework 

| SQLModel             | ORM & Data Models 

| PostgreSQL           | Relational Database 

| Supabase             | Hosted PostgreSQL Database 

| python-dotenv        | Environment Variables 

| Uvicorn              | ASGI Server 

| Poetry               | Dependency & Environment Management 

| Mypy                 | Static Type Checking 

| Swagger UI           | API Testing & Documentation 

## 🗄️ Database Architecture

The application uses PostgreSQL through Supabase.

FastAPI Application
        │
        ▼
   SQLModel ORM
        │
        ▼
   Database Engine
        │
        ▼
 PostgreSQL / Supabase

Database configuration is separated into:

todos/config/db.py

This keeps database connection logic separate from API routes and models.

## 🔐 Environment Variables

Database credentials should never be hard-coded inside the source code.

The project uses a .env file:

DB_URL=postgresql://username:password@host:5432/database

Environment variables are loaded using python-dotenv:

from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("DB_URL")

## Install the package with Poetry:

poetry add python-dotenv

The .env file should be included in .gitignore:

.env

This prevents sensitive database credentials from being pushed to GitHub.

## 🧩 Database Configuration

The database engine is created in:

todos/config/db.py

Example:

from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("DB_URL")

engine = create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(engine)
## 📦 Data Models

The main Todo model is defined in:

todos/models/todos.py
Todo Model
class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    is_completed: bool
The model represents the database table and defines its fields.

Update Model

A separate model is used for update operations:

class UpdateTodo(SQLModel):
    title: str | None
    description: str | None
    is_completed: bool | None

This allows partial updates without requiring every field.

## 🔄 CRUD Operations

The project demonstrates complete CRUD functionality.

**1. Get All Todos**
GET /gettodos

Fetches all Todo records from the database.

**2. Filter Todos**
GET /get_todo

Uses SQLModel's where() condition to filter records.

Example:

statement = select(Todo).where(Todo.title == "zarlish")
**3. Create Todo**
POST /create_todo

Example request body:

{
    "title": "Learn FastAPI",
    "description": "Practice FastAPI and SQLModel",
    "is_completed": false
}
**4. Update Todo**
PUT /update_todo/{id}

The API receives the Todo ID through a path parameter and updates the selected record.

**5. Delete Todo**
DELETE /delete_todo/{todo_id}

Deletes a Todo record using its database ID.

## 📥 CSV Export

The project also includes an endpoint for exporting Todo data as a CSV file.

GET /download_csv

The endpoint:

Opens a database session
Fetches Todo records
Converts the data into CSV format
Returns the CSV file as a response
## 🔎 API Parameters

The project demonstrates different ways to receive data from a client.

Path Parameter
GET /students/{student_id}

Example:

/students/5
Query Parameter
GET /students?name=zarlish
Request Body

Used with POST and PUT requests:
{
    "title": "FastAPI",
    "description": "Backend development",
    "is_completed": false
}
📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI
http://localhost:8080/docs

## Swagger allows you to:

View available endpoints
Enter parameters
Send requests
Test POST/PUT/DELETE APIs
View request and response schemas
Debug API behavior
# ⚙️ Installation & Setup
**1. Clone Repository**
git clone https://github.com/devzarmeen/fastapi-backend-api-integration.git
cd fastapi-backend-api-integration
**2. Install Dependencies**
This project uses Poetry.
poetry install
**3. Activate Poetry Environment**
poetry shell
Or run commands directly:
poetry run <command>
**4. Configure Environment Variables**

Create a .env file in the project root:

DB_URL=your_postgresql_connection_string

Do not commit this file to GitHub.

**5. Run the Application**
poetry run uvicorn todos.DynamicTodosAppSQLModel:app --host 127.0.0.1 --port 8080 --reload

Application:

http://127.0.0.1:8080

**Swagger:**

http://127.0.0.1:8080/docs
## 🧪 Testing

API endpoints can be tested using:

Swagger UI
Postman
REST Client
Python requests

Swagger provides the easiest way to test the APIs directly from the browser.

## 🔍 Type Checking

The project uses Mypy for static type checking.

Example:

mypy todos/DynamicTodosAppSQLModel.py

Mypy helps identify type-related issues before runtime.

## 📖 Learning Documentation

The repository also contains separate documentation covering:

FastAPI fundamentals
API parameters
Request & response handling
PostgreSQL connection
SQLModel
Poetry & Uvicorn
API integration concepts

These files provide step-by-step learning material alongside the practical implementation.

# 🎯 Project Goals

This project was created to build practical understanding of:

FastAPI
   ↓
REST APIs
   ↓
Request Handling
   ↓
SQLModel
   ↓
PostgreSQL
   ↓
CRUD Operations
   ↓
API Documentation
   ↓
Production-oriented Backend Structure
# 🚀 Future Improvements

Possible improvements include:

Authentication & Authorization
JWT Authentication
Better project modularization
Pydantic response schemas
Global exception handling
Automated testing with Pytest
Database migrations with Alembic
Pagination
Advanced filtering & sorting
Docker support
CI/CD pipeline
Production deployment

# 👩‍💻 Author

Zarmeen Rasool

# AI Engineer | Backend & AI Development

Connect
GitHub: https://github.com/devzarmeen
LinkedIn: https://www.linkedin.com/in/zarmeenrasool/
