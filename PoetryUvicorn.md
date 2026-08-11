Build Function using Python Flask Server in FAST API Frame work

# How to build  Api Functions what does it means 
# how to run that functions


To understand the core backend development we should know how to call third party softwares like (send grid, Stripe, Door Dash and AI Models etc) and how to refine our own models and run with our own functions  

# NPM (Node Package manager)    used in  frontend
It help us to install load and manage the Already used codes by people 

If we want to send the application to other person we don't need to send complete files of packages we just send package json file for information to install packages 

## Poetry Python (PP)       Used in backend

**LINK** : https://python-poetry.org/

It brings thing in automation and more flexible 

## Step 1: Install Poetry

pipx install poetry

**if you don't have pipx:**

pip install poetry

**Verify the Installation:**

poetry --version 

## Step 2: Create a Project Folder

**Wed, Jul 8 at 9:47 PM
4july2026.ipynb
File
is file ko check kro khyn urdu ma comment to nhi ha khyn speeling mistake ha to batao kahan ha 
4july2026(1).ipynb
File
is file ko check kro khyn urdu ma comment to nhi ha khyn speeling mistake ha to batao kahan ha  kahan kahan kya kya ha wo batao kis block ma kya error ha wo batao  name sy ky list ma ha tuple ma ha access tuuple is trha 
04_Linear_and_Logistic_Regression.ipynb
File
koi conversion program h is file ma 
ma ny model ko save krna ha titnaic ma direct notebook ma nhi mujhy usky according ya code do or ya error kun ha 

Tumhare code mein sirf ek typo (spelling mistake) hai.

Tumhara code
N, X = map(int, input().split())

marks = []

for _ in range(X):
    marks.append(list(map(float, input().split())))

for student in zip(*makks):
    print(sum(student) / len(student))
❌ Mistake

Tumne likha hai:

zip(*makks)

Variable ka naam makks nahi hai.

Tumne list ka naam upar banaya tha:

marks = []

Isliye yahan bhi marks hi use hoga.

✅ Correct Code
N, X = map(int, input().split())

marks = []

for _ in range(X):
    marks.append(list(map(float, input().split())))

for student in zip(*marks):
    print(sum(student) / len(student))
Agar makks likhoge to error aayega:
NameError: name 'makks' is not defined
Ek aur chhoti baat

Tumne N variable use nahi kiya hai.

Ye bilkul theek hai. HackerRank input format ki wajah se N read karna zaroori hai, lekin logic mein uski zarurat nahi padti.

So final code is:

N, X = map(int, input().split())

marks = []

for _ in range(X):
    marks.append(list(map(float, input().split())))

for student in zip(*marks):
    print(sum(student) / len(student))

Ye HackerRank par 100% accepted solution hai.

Assume same table:

employees(
    employee_id,
    employee_name,
    department,
    salary,
    city,
    age
)

Question 26

Un employees ka employee_name, department, aur city display karein jo Karachi se hain aur HR department mein nahi hain.

Question 27

Har department ki total salary calculate karein aur result ko total salary (highest to lowest) order mein display karein.

Question 28

Un departments ko display karein jahan average employee age 30 saal se zyada hai.

Question 29

Employees ki average salary calculate karein, phir sirf un employees ko display karein jinki salary average salary se zyada hai.

💡 Is question mein thoda logic use hoga.

Question 30

Har city ke liye:

Total employees
Highest salary
Lowest salary

Ek hi result mein display karein. transalte in english and also give solution

Question 26
English

Display the employee name, department, and city of employees who are from Karachi and are not in the HR department.

SQL Solution
SELECT employee_name, department, city
FROM employees
WHERE city = 'Karachi'
  AND department <> 'HR';
Question 27
English

Calculate the total salary for each department and display the results in descending order of total salary.

SQL Solution
SELECT department,
       SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;
Question 28
English

Display the departments where the average employee age is greater than 30 years.

SQL Solution
SELECT department,
       AVG(age) AS average_age
FROM employees
GROUP BY department
HAVING AVG(age) > 30;
Question 29
English

Calculate the average salary of all employees, then display only those employees whose salary is greater than the average salary.

💡 This question requires using a subquery.

SQL Solution
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
Question 30
English

For each city, display:

Total number of employees
Highest salary
Lowest salary

Show all the results in a single query.

SQL Solution
SELECT city,
       COUNT(*) AS total_employees,
       MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM employees
GROUP BY city;
Today 8:44 PM
poerty ko setup krny ky liya jo steps or commands hain folders kaisay bnty root sy wo english ma step y step  batao 
Poetry Setup Guide (Step by Step)
# Step 1: Install Poetry

**If Poetry is not installed, run:**

- pipx install poetry

**Or if you don't have pipx:**

- pip install poetry

**Verify the installation:**

poetry --version

## Step 2: Create a Project Folder

**Create a new project directory**

- mkdir fastapi-backend-api-integration

**Open Power Shell And Execute commands**

- PS C:\Users\World> E:
- PS E:\> cd Internship
- PS E:\Internship> cd fastapi-backend-api-integration
- PS E:\Internship\fastapi-backend-api-integration> pwd
- PS E:\Internship\fastapi-backend-api-integration>

## Step 3: Install Poetry Environment

- poetry install

## Step 4: Install Required Packages

- poetry add fastapi uvicorn sqlalchemy pydantic python-dotenv

- poetry add requests

- poetry add psycopg2-binary

## Automated Testing 
In python the tool pytest tool is used

The code foe testing software  will be written in tests folder this is called Automated testing and we will use library pytest