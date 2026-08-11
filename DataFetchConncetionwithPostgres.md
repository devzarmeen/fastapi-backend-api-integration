# PostgreSQL, Connection Strings, ORM, and SQLModel

## 1. Setting Up PostgreSQL on the Cloud

Once we have set up our **PostgreSQL database on the cloud**, we may want to connect it to tools like **TablePlus**.

For this connection, we need a **connection string**.

The connection string contains the information required to establish a connection with the PostgreSQL database.

## 2. Connecting PostgreSQL with Our Code

If we want to connect the cloud PostgreSQL database with our **FastAPI application**, we also need a **connection string**.

# The basic idea is:

FastAPI Application
       ↓
Connection String
       ↓
PostgreSQL Database


## 3. What is an ORM?

We usually use an intermediate library called an **ORM (Object-Relational Mapping)**.

An ORM is a library that makes database operations easier for us.

Instead of manually writing all the database-related code, the ORM provides built-in functionality for:

* Connecting to the database
* Creating tables
* Managing tables
* Performing CRUD operations
* Working with database queries

The ORM acts as an intermediate layer between our FastAPI application and the database.

FastAPI
   ↓
 ORM
   ↓
PostgreSQL

## 4. Can We Connect FastAPI Directly to PostgreSQL?

Yes, we can connect to PostgreSQL without using an ORM.

However, without an ORM, we would have to manually write much more database-related code.

An ORM provides many of these functionalities for us, making database development easier and more structured.


## 5. ORM Options

For PostgreSQL, we can use different ORM libraries, such as:

* SQLModel
* SQLAlchemy
* Prisma
* Other database libraries/tools

In our project, we will use **SQLModel**.

## 6. SQLModel

**SQLModel** is a modern and structured ORM that makes working with databases easier.

It is designed to work well with **FastAPI** and **Pydantic-style models**.

SQLModel helps us simplify:

* Database connections
* Table creation
* Table management
* Database queries
* CRUD operations

Official documentation:

[SQLModel Documentation](https://sqlmodel.tiangolo.com/?utm_source=chatgpt.com)

## 7. ORM Has Its Own Syntax

Different ORMs provide their own way of writing database operations.

# For example, in traditional SQL, we might write:

SELECT * FROM users;

Other ORM systems provide their own methods or syntax for performing similar operations.

For example, an ORM may provide methods such as:

get()

So, instead of manually writing SQL queries for every operation, we can use the syntax and methods provided by the ORM.

## 8. ORM Depends on the Database Technology

The tools and libraries we use can vary depending on the database.

# For example:

FastAPI
   ↓
SQLModel / SQLAlchemy
   ↓
PostgreSQL


For another type of database, such as MongoDB, we would typically use different database libraries/tools.

The important point is that the database technology determines which libraries or database abstraction tools are appropriate.

# 9. Important Features of an ORM

An ORM generally provides several important features.

### 1. Database Connection

First, we need to know:

> How can we create a connection with the database?

For creating the database connection, we use a **connection string**.

We usually create a function that receives the connection string and creates the database connection for our application.

# Conceptually:

Connection String
       ↓
ORM
       ↓
Database Connection
       ↓
PostgreSQL
This database connection functionality is an important part of working with an ORM.

### 2. Table / Schema Creation

The second important feature is the ability to define and create database tables.

The ORM provides its own syntax for defining models/tables.

For example, instead of manually writing SQL `CREATE TABLE` statements, we can define our table structure using the ORM's model syntax.

### 3. CRUD Operations

The third important feature is performing **CRUD operations** on our tables.

# CRUD stands for:

C → Create
R → Read
U → Update
D → Delete

The ORM provides methods and functionality that make these operations easier to perform.

# 10. Why Use SQLModel?

We can work with PostgreSQL without SQLModel or another ORM.

However, without an ORM, we would have to manually write and manage much of the database-related code.

SQLModel provides many of these features in a structured and convenient way.

Therefore, in our project, we will use:
FastAPI
    ↓
SQLModel
    ↓
PostgreSQL

SQLModel will act as the database abstraction layer between our FastAPI application and PostgreSQL.

# 11. Our Learning Flow

We will follow this basic flow:

1. Set up PostgreSQL database
            ↓
2. Get the PostgreSQL connection string
            ↓
3. Use SQLModel in our FastAPI project
            ↓
4. Create the database connection
            ↓
5. Define database models/tables
            ↓
6. Create/manage tables
            ↓
7. Perform CRUD operations

This will allow our **FastAPI application** to communicate with the **PostgreSQL database** in a structured way using **SQLModel**.
