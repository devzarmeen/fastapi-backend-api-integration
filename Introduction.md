##       -------------------  Software Life Cycle  --------------------

1. Idea

2. Software Requirements Specification (SRS) / Documentation / Requirements Elicitation

3. Design (The primary design tool is Figma) / UI/UX

4. Development / Coding

5. Deployment / DevOps

6. Marketing

7. Maintenance


##         ----------------  Software Development Phase  -------------------

# 1. Frontend

- JavaScript
- TypeScript          (These two are programming languages.)
- Java
- Kotlin
- Dart
- Objective-C
- Swift

## Frameworks

- React.js
- React Native
- Flutter
- Next.js


# 2. Backend

- Python
- Node.js
- PHP
- Ruby on Rails
- Java (Used rarely)
- C#

## Frameworks

- FastAPI
- Flask
- Django
- Next.js
- Spring
- Express.js
- NestJS
- .NET


# 3. Database

- Firebase
- Firestore
- PostgreSQL
- MongoDB
- MySQL
- Oracle
- SQLite
- Amazon Aurora DB
- Couchbase DB


# Why Frontend and Backend are Two Different Things

The main reason is **security**.

Users can only see the frontend (icons, messages, buttons, forms, etc.).

The backend contains the main code and business logic (such as addition, subtraction, authentication, validation, and many other operations).

Communication between the frontend, backend, and database happens through different protocols.

The most commonly used protocol is **Hypertext Transfer Protocol (HTTP)**.


## HTTP

HTTP handles requests and responses.

The frontend sends a request to the backend.

The backend sends a request to the database.

The database receives the request, processes it, and sends a response back to the backend.

Finally, the backend sends the response to the frontend.

This entire communication process is made possible through HTTP.


# Any frontend language/framework can communicate with any backend language/framework using the same standard protocol, which is HTTP.


# AND


# Any backend language/framework can communicate with any database through HTTP.


##      ----------------  Backend Development Life Cycle  -----------------

The two major responsibilities of the backend are:

- Receive requests from the frontend and send responses back to the frontend.
- Send requests to the database, receive responses, and implement the business logic.


## Life Cycle

1. Request Received (A function receives the request.)

2. The code responsible for handling the frontend request is written here.

   We implement business logic here, such as loops, functions, conditions, lists, etc.

3. The same function processes the request and sends the appropriate response.

4. If the frontend requests to save data, the function also communicates with the database.


# SendGrid

5. If the function receives a request to send an email, it creates a connection with a third-party service called **SendGrid**.

   SendGrid is a third-party software that sends emails to the required recipients.


# Stripe
**Link**: https://docs.stripe.com/api

6. If the function receives a request to process a card payment, we use the third-party service **Stripe**.


# DoorDash

7. If the function receives a request to deliver an order, we use the third-party service **DoorDash**.


# AI Model

8. If the function receives a signup request where uploading a picture is mandatory, and the condition is that the picture must contain a human, then an AI model is required.

The AI model processes the image to determine whether it contains a human or not.

Based on the result, it sends the response back to the backend, which then returns the appropriate response to the frontend.

GPT, Gemini, and Stability are AI models that we call according to our application requirements.


##        ----------------  AI Model Development Life Cycle  --------------

1. Trained Model / Output Form

1.1 Data / Images

1.2 EDA (Exploratory Data Analysis)

1.3 Preprocessing

1.4 Scaling

1.5 Training and Testing

1.6 Evaluation

1.7 Fine-Tuning


##       ------------------  Three Options for Backend Development  -----------------

These three frameworks focus on both **custom business logic** and **third-party integrations** at the same time.

The request handling and response handling code is already built into these frameworks.

- Django

- FastAPI

- Flask

## API 

All process of request, response, third party handling, and database handling is also known Application Programming Interface(API)

Communication medium between two applications is API 

