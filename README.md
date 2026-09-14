# 📚 Student Management API — Complete README

Below is a **beginner-friendly complete README** for the project you built from **Phase 1 → Phase 5**.

It covers **FastAPI, PostgreSQL, SQLAlchemy ORM, Pydantic, CRUD, relationships, JOINs, reports, password hashing, JWT authentication, Swagger, Postman, project structure, installation, routes, sample data, and interview questions**.

---

# 🎓 Student Management API

A beginner-friendly **Student Management REST API** built using:

```text
FastAPI
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL
```

The project started with basic CRUD and gradually added:

```text
Phase 1 → Student CRUD
Phase 2 → Course CRUD
Phase 3 → Marks + Relationships
Phase 4 → JOINs + Reports
Phase 5 → Authentication + JWT
```

---

# 🚀 1. Project Overview

The Student Management API manages:

* 👨‍🎓 Students
* 📚 Courses
* 📝 Marks
* 📊 Reports
* 🔐 Users
* 🔑 Authentication

The application communicates with PostgreSQL through SQLAlchemy ORM.

```text
                 FastAPI
                    │
                    ↓
              API Endpoints
                    │
                    ↓
             SQLAlchemy ORM
                    │
                    ↓
               PostgreSQL
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
    students     courses      marks
                    │
                    ↓
                  users
```

---

# 🛠️ 2. Technologies Used

| Technology  | Purpose                    |
| ----------- | -------------------------- |
| Python      | Programming language       |
| FastAPI     | Build REST APIs            |
| Pydantic    | Request validation         |
| SQLAlchemy  | ORM/database communication |
| PostgreSQL  | Database                   |
| Psycopg2    | PostgreSQL driver          |
| Uvicorn     | Run FastAPI server         |
| Passlib     | Password hashing           |
| Bcrypt      | Password-hashing algorithm |
| Python-JOSE | JWT creation/verification  |
| Swagger UI  | API testing/documentation  |
| Postman     | API testing                |

---

# 📁 3. Project Structure

```text
student_management_api/
│
├── main.py
├── database.py
├── security.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── mark.py
│   └── user.py
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── mark.py
│   └── user.py
│
└── routers/
    ├── __init__.py
    ├── students.py
    ├── courses.py
    ├── marks.py
    ├── reports.py
    └── auth.py
```

---

# 🧠 4. What Each Folder Does

## `main.py`

Main entry point of the FastAPI application.

It:

* Creates FastAPI app
* Imports models
* Creates database tables
* Includes routers

---

## `database.py`

Creates the connection between:

```text
Python
  ↓
SQLAlchemy
  ↓
PostgreSQL
```

Example:

```python
DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"
```

---

## `models/`

Contains SQLAlchemy ORM models.

```text
models/
   ↓
Database table structure
```

For example:

```python
class Student(Base):
```

represents:

```text
students table
```

---

## `schemas/`

Contains Pydantic models.

```text
schemas/
   ↓
API input validation
```

For example:

```python
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    city: str
```

---

## `routers/`

Contains API endpoints.

```text
routers/
   ↓
API URLs
```

Examples:

```text
/students
/courses
/marks
/reports
/auth
```

---

## `security.py`

Contains authentication logic:

```text
Password Hashing
       +
Password Verification
       +
JWT Creation
       +
JWT Verification
```

---

# 🗄️ 5. Database Design

The main tables are:

```text
students
courses
marks
users
```

Relationship:

```text
              students
                  │
                  │ student_id
                  │
                  ↓
                marks
                  ↑
                  │ course_id
                  │
                  │
               courses
```

Authentication:

```text
users
  │
  ├── user_id
  ├── username
  ├── email
  ├── password
  └── role
```

---

# 👨‍🎓 6. Student Model

`models/student.py`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):

    __tablename__ = "students"

    student_id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    age = Column(Integer)

    email = Column(String)

    city = Column(String)

    marks = relationship(
        "Mark",
        back_populates="student"
    )
```

### Student fields

| Field        | Type    | Purpose      |
| ------------ | ------- | ------------ |
| `student_id` | Integer | Primary key  |
| `name`       | String  | Student name |
| `age`        | Integer | Age          |
| `email`      | String  | Email        |
| `city`       | String  | City         |

---

# 📚 7. Course Model

`models/course.py`

```python
class Course(Base):

    __tablename__ = "courses"

    course_id = Column(
        Integer,
        primary_key=True
    )

    course_name = Column(String)

    duration = Column(Integer)

    marks = relationship(
        "Mark",
        back_populates="course"
    )
```

Example:

```text
1 → Python
2 → SQL
3 → FastAPI
4 → Java
5 → Data Science
```

---

# 📝 8. Mark Model

`models/mark.py`

```python
class Mark(Base):

    __tablename__ = "marks"

    mark_id = Column(
        Integer,
        primary_key=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    marks = Column(Integer)

    student = relationship(
        "Student",
        back_populates="marks"
    )

    course = relationship(
        "Course",
        back_populates="marks"
    )
```

The `marks` table connects:

```text
Student ←→ Marks ←→ Course
```

---

# 🔐 9. User Model

`models/user.py`

```python
class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        default="student"
    )
```

---

# 🔄 10. ORM Explained

ORM means:

> Object Relational Mapping

It allows Python objects to represent database tables.

Without ORM:

```sql
SELECT * FROM students;
```

With SQLAlchemy ORM:

```python
db.query(Student).all()
```

So:

```text
Python Class
     ↓
SQLAlchemy ORM
     ↓
Database Table
```

---

# ✅ 11. Pydantic vs SQLAlchemy

This is an important concept.

### Pydantic

Used for:

```text
API validation
```

Example:

```python
class StudentCreate(BaseModel):
    name: str
    age: int
```

### SQLAlchemy

Used for:

```text
Database table
```

Example:

```python
class Student(Base):
```

Remember:

```text
Pydantic
   ↓
"What data can the API receive?"

SQLAlchemy
   ↓
"How is the database table represented?"
```

---

# 📌 12. API CRUD

CRUD means:

```text
C → Create
R → Read
U → Update
D → Delete
```

| Operation | HTTP   |
| --------- | ------ |
| Create    | POST   |
| Read      | GET    |
| Update    | PUT    |
| Delete    | DELETE |

---

# 👨‍🎓 13. Student CRUD

### Get all students

```http
GET /students/
```

### Get one student

```http
GET /students/1
```

### Create student

```http
POST /students/
```

Example:

```json
{
    "name": "Ravi Kumar",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

### Update

```http
PUT /students/1
```

### Delete

```http
DELETE /students/1
```

---

# 📚 14. Course CRUD

```text
GET    /courses/
POST   /courses/
GET    /courses/{id}
PUT    /courses/{id}
DELETE /courses/{id}
```

---

# 📝 15. Marks CRUD

```text
GET    /marks/
POST   /marks/
GET    /marks/{id}
PUT    /marks/{id}
DELETE /marks/{id}
GET    /marks/search/
```

Example:

```text
GET /marks/search/?minimum=80
```

This returns marks greater than or equal to `80`.

---

# 🔗 16. Relationships

A student can have multiple marks.

```text
Student
   │
   ├── Mark
   ├── Mark
   └── Mark
```

This is a:

```text
One-to-Many relationship
```

A course can also have multiple marks:

```text
Course
   │
   ├── Mark
   ├── Mark
   └── Mark
```

---

# 🔑 17. ForeignKey

In `marks`:

```python
student_id = Column(
    Integer,
    ForeignKey("students.student_id")
)
```

means:

```text
marks.student_id
       ↓
students.student_id
```

And:

```python
course_id = Column(
    Integer,
    ForeignKey("courses.course_id")
)
```

means:

```text
marks.course_id
       ↓
courses.course_id
```

---

# 🔄 18. `relationship()`

Example:

```python
marks = relationship(
    "Mark",
    back_populates="student"
)
```

This allows:

```python
student.marks
```

to access the marks belonging to that student.

Similarly:

```python
mark.student
```

can access the related student.

---

# 🔀 19. JOINs

Phase 4 introduced database JOINs.

Example:

```python
result = (
    db.query(
        Student.name,
        Course.course_name,
        Mark.marks
    )
    .join(
        Mark,
        Student.student_id == Mark.student_id
    )
    .join(
        Course,
        Course.course_id == Mark.course_id
    )
    .all()
)
```

Conceptually:

```text
students
    │
    │ JOIN
    ↓
marks
    │
    │ JOIN
    ↓
courses
```

Result:

```text
Ravi    Python    85
Ravi    SQL       90
Ravi    FastAPI   88
```

---

# 📊 20. Reports

Your project includes report APIs such as:

```text
/reports/student-marks
/reports/student/{student_id}
/reports/search/by-city
/reports/search/
/reports/students-with-marks
/reports/course-students
/reports/student-average/{student_id}
```

Your Swagger documentation shows these report endpoints. 

---

# 📈 21. Average Marks

SQLAlchemy provides:

```python
func.avg(Mark.marks)
```

Example:

```python
db.query(
    Student.name,
    func.avg(Mark.marks).label("average_marks")
)
```

For Ravi:

```text
85
90
88
82
```

Average:

```text
(85 + 90 + 88 + 82) / 4

= 86.25
```

---

# 🔐 22. Authentication

Phase 5 introduced authentication.

Authentication asks:

> **Who are you?**

Authorization asks:

> **What are you allowed to do?**

Current project has:

```text
Register
   ↓
Password Hashing
   ↓
Login
   ↓
JWT
   ↓
Protected API
```

---

# 👤 23. Registration

Endpoint:

```http
POST /auth/register
```

Example:

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

The password is hashed before storing it.

```text
python123
    ↓
bcrypt
    ↓
$2b$12$.........
    ↓
PostgreSQL
```

The real password should not be stored directly.

---

# 🔑 24. Password Hashing

`security.py` uses:

```python
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
```

Hash:

```python
def hash_password(password: str):
    return pwd_context.hash(password)
```

Verify:

```python
def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
```

---

# 🔓 25. Login

Endpoint:

```http
POST /auth/login
```

Because the project uses `OAuth2PasswordRequestForm`, login is sent as:

```text
x-www-form-urlencoded
```

Example:

```text
username = ravi
password = python123
```

The API returns:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

Your Swagger documentation shows `/auth/register` and `/auth/login`. 

---

# 🪪 26. JWT

JWT means:

```text
JSON Web Token
```

It is used to prove that a user has successfully authenticated.

Flow:

```text
Username
   +
Password
   ↓
Login
   ↓
Verify password
   ↓
Create JWT
   ↓
Return token
```

---

# 🔍 27. JWT Payload

Your token contains information similar to:

```json
{
    "sub": "1",
    "username": "ravi",
    "role": "student",
    "exp": 1789413223
}
```

### `sub`

Subject/user ID.

```text
sub = 1
```

### `username`

```text
ravi
```

### `role`

```text
student
```

### `exp`

Token expiration time.

---

# 🛡️ 28. `get_current_user()`

This function checks the JWT.

```python
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
```

---

# 🔒 29. Protected Route

Your current protected route is:

```http
GET /students/profile
```

Code:

```python
@router.get("/profile")
def student_profile(
    current_user = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user": current_user
    }
```

The important line is:

```python
Depends(get_current_user)
```

It means:

```text
Request
   ↓
get_current_user()
   ↓
Check JWT
   ↓
Valid?
 ┌─┴─┐
NO  YES
 ↓    ↓
401  API
```

---

# ⚠️ 30. Route Order

This is an important lesson from your project.

You had:

```python
@router.get("/{id}")
```

before:

```python
@router.get("/profile")
```

Then:

```text
/students/profile
```

was interpreted as:

```text
/students/{id}
```

and FastAPI tried:

```python
int("profile")
```

which caused:

```text
422 Unprocessable Entity
```

### Correct order

```python
@router.get("/profile")
```

must come before:

```python
@router.get("/{id}")
```

Remember:

```text
Static route
    ↓
Dynamic route
```

---

# 🧪 31. Swagger UI

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger provides interactive API testing.

Your Swagger currently exposes Students, Courses, Marks, Reports and Authentication sections.  

---

# 📮 32. Postman

You can also test the APIs using Postman.

### Login

```text
POST
http://127.0.0.1:8000/auth/login
```

Body:

```text
x-www-form-urlencoded
```

```text
username    ravi
password    python123
```

---

# 🔑 33. Postman Bearer Token

After login:

```text
access_token
```

Copy it.

Then:

```text
GET
http://127.0.0.1:8000/students/profile
```

Go to:

```text
Authorization
    ↓
Type: Bearer Token
    ↓
Paste JWT
```

Then:

```text
Send
```

Expected:

```json
{
    "message": "You are authenticated",
    "user": {
        "sub": "1",
        "username": "ravi",
        "role": "student"
    }
}
```

---

# 📦 34. Installation

Create project:

```bash
mkdir student_management_api
cd student_management_api
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install main packages:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

Install authentication:

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

Install OAuth2 form support:

```bash
pip install python-multipart
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

# ▶️ 35. Run the Project

```bash
uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🧪 36. Sample Student Data

```json
{
    "name": "Ravi Kumar",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

```json
{
    "name": "Priya Sharma",
    "age": 22,
    "email": "priya@gmail.com",
    "city": "Bangalore"
}
```

```json
{
    "name": "Amit Reddy",
    "age": 20,
    "email": "amit@gmail.com",
    "city": "Hyderabad"
}
```

```json
{
    "name": "Sneha Patel",
    "age": 23,
    "email": "sneha@gmail.com",
    "city": "Mumbai"
}
```

```json
{
    "name": "Arjun Rao",
    "age": 21,
    "email": "arjun@gmail.com",
    "city": "Chennai"
}
```

---

# 📚 37. Sample Course Data

```json
{
    "course_name": "Python",
    "duration": 6
}
```

```json
{
    "course_name": "SQL",
    "duration": 3
}
```

```json
{
    "course_name": "FastAPI",
    "duration": 4
}
```

```json
{
    "course_name": "Java",
    "duration": 5
}
```

```json
{
    "course_name": "Data Science",
    "duration": 8
}
```

---

# 📝 38. Sample Marks Data

```json
{
    "student_id": 1,
    "course_id": 1,
    "marks": 85
}
```

```json
{
    "student_id": 1,
    "course_id": 2,
    "marks": 90
}
```

```json
{
    "student_id": 1,
    "course_id": 3,
    "marks": 88
}
```

```json
{
    "student_id": 1,
    "course_id": 4,
    "marks": 82
}
```

```json
{
    "student_id": 2,
    "course_id": 1,
    "marks": 78
}
```

```json
{
    "student_id": 2,
    "course_id": 2,
    "marks": 85
}
```

```json
{
    "student_id": 2,
    "course_id": 5,
    "marks": 91
}
```

```json
{
    "student_id": 3,
    "course_id": 1,
    "marks": 92
}
```

```json
{
    "student_id": 3,
    "course_id": 3,
    "marks": 87
}
```

```json
{
    "student_id": 3,
    "course_id": 5,
    "marks": 89
}
```

```json
{
    "student_id": 4,
    "course_id": 2,
    "marks": 75
}
```

```json
{
    "student_id": 4,
    "course_id": 4,
    "marks": 80
}
```

```json
{
    "student_id": 4,
    "course_id": 5,
    "marks": 84
}
```

```json
{
    "student_id": 5,
    "course_id": 1,
    "marks": 88
}
```

```json
{
    "student_id": 5,
    "course_id": 2,
    "marks": 93
}
```

```json
{
    "student_id": 5,
    "course_id": 3,
    "marks": 90
}
```

---

# 👤 39. Sample User Data

### Ravi

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

### Priya

```json
{
    "username": "priya",
    "email": "priya@gmail.com",
    "password": "fastapi123"
}
```

### Amit

```json
{
    "username": "amit",
    "email": "amit@gmail.com",
    "password": "sql12345"
}
```

### Sneha

```json
{
    "username": "sneha",
    "email": "sneha@gmail.com",
    "password": "student123"
}
```

### Arjun

```json
{
    "username": "arjun",
    "email": "arjun@gmail.com",
    "password": "python456"
}
```

---

# 🛣️ 40. Complete API Routes

## 🏠 Home

```text
GET /
```

## 👨‍🎓 Students

```text
GET    /students/
GET    /students/profile
GET    /students/{id}
POST   /students/
PUT    /students/{id}
DELETE /students/{id}
```

## 📚 Courses

```text
GET    /courses/
POST   /courses/
GET    /courses/{id}
PUT    /courses/{id}
DELETE /courses/{id}
GET    /courses/{id}/marks
```

## 📝 Marks

```text
GET    /marks/
POST   /marks/
GET    /marks/{id}
PUT    /marks/{id}
DELETE /marks/{id}
GET    /marks/search/
```

## 📊 Reports

```text
GET /reports/student-marks
GET /reports/student/{student_id}
GET /reports/search/by-city
GET /reports/search/
GET /reports/students-with-marks
GET /reports/course-students
GET /reports/student-average/{student_id}
```

## 🔐 Authentication

```text
POST /auth/register
POST /auth/login
```

---

# 🔄 41. Complete Project Flow

```text
                         CLIENT
                           │
                    Swagger / Postman
                           │
                           ↓
                        FastAPI
                           │
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
        Students        Courses         Marks
            │              │              │
            └──────────────┼──────────────┘
                           ↓
                     SQLAlchemy ORM
                           │
                           ↓
                       PostgreSQL
```

Authentication:

```text
User
 ↓
Register
 ↓
Hash Password
 ↓
users table
 ↓
Login
 ↓
Verify Password
 ↓
JWT Token
 ↓
Bearer Token
 ↓
get_current_user()
 ↓
Protected API
```

---

# 🎯 42. What You Learned

### Phase 1

```text
FastAPI
Pydantic
PostgreSQL
SQLAlchemy
CRUD
```

### Phase 2

```text
Multiple models
Multiple routers
APIRouter
Course CRUD
```

### Phase 3

```text
ForeignKey
relationship()
One-to-Many
Student-Marks
Course-Marks
```

### Phase 4

```text
JOIN
filter()
group_by()
func.avg()
Reports
```

### Phase 5

```text
Authentication
Password Hashing
Bcrypt
JWT
OAuth2
Bearer Token
Depends()
Protected Routes
get_current_user()
```

---

# 🎤 43. Beginner Interview Questions

### 1. What is FastAPI?

FastAPI is a Python framework used to build APIs.

---

### 2. What is an API?

API means **Application Programming Interface**.

It allows applications to communicate with each other.

---

### 3. What is CRUD?

```text
Create → POST
Read   → GET
Update → PUT
Delete → DELETE
```

---

### 4. What is SQLAlchemy?

SQLAlchemy is a Python library used to communicate with databases.

Its ORM allows database tables to be represented as Python classes.

---

### 5. What is ORM?

ORM means:

```text
Object Relational Mapping
```

It maps Python objects/classes to database tables.

---

### 6. What is Pydantic?

Pydantic validates API request data.

---

### 7. What is a Foreign Key?

A Foreign Key connects one table to another.

Example:

```python
ForeignKey("students.student_id")
```

---

### 8. What is `relationship()`?

It allows SQLAlchemy objects to navigate between related records.

Example:

```python
student.marks
```

---

### 9. What is JOIN?

JOIN combines related records from multiple tables.

---

### 10. What is JWT?

JWT stands for:

```text
JSON Web Token
```

It is commonly used to authenticate API requests.

---

### 11. What is password hashing?

Password hashing converts a password into a one-way hashed value before storage.

```text
python123
     ↓
bcrypt
     ↓
hashed value
```

---

### 12. What is authentication?

Authentication answers:

> Who is the user?

---

### 13. What is authorization?

Authorization answers:

> What is the user allowed to do?

---

### 14. What is `Depends()`?

`Depends()` allows FastAPI to execute a dependency before an endpoint.

Example:

```python
current_user = Depends(get_current_user)
```

---

### 15. What does HTTP 401 mean?

```text
401 Unauthorized
```

The request is not properly authenticated.

---

### 16. What does HTTP 422 mean?

```text
422 Unprocessable Entity
```

The request data could not be validated/parsed according to the endpoint's expected parameters.

---

# ⭐ 44. Important Concepts to Remember

```text
FastAPI
   ↓
Creates API

Pydantic
   ↓
Validates API data

SQLAlchemy
   ↓
Communicates with database

PostgreSQL
   ↓
Stores data

APIRouter
   ↓
Organizes API routes

ForeignKey
   ↓
Connects tables

relationship()
   ↓
Connects ORM objects

JOIN
   ↓
Combines table data

Passlib/Bcrypt
   ↓
Protects passwords

JWT
   ↓
Authenticates requests

Depends()
   ↓
Runs dependencies

get_current_user()
   ↓
Checks JWT
```

---

# 🏆 45. Final Architecture

```text
                  STUDENT MANAGEMENT API
                           │
                           ↓
                        FastAPI
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
     Routers             Schemas            Security
        │                  │                  │
        │                  │          ┌───────┴───────┐
        │                  │          ↓               ↓
        │              Pydantic    Password          JWT
        │                           Hashing
        ↓
 ┌──────┼────────┬──────────┬──────────┐
 ↓      ↓        ↓          ↓          ↓
Student Course  Marks    Reports      Auth
 │       │       │          │           │
 └───────┴───────┴──────────┘           │
             │                           │
             ↓                           ↓
       SQLAlchemy ORM              Authentication
             │                           │
             └───────────┬───────────────┘
                         ↓
                    PostgreSQL
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
          students    courses     marks
                                   
                         users
```

---

# 🚀 46. Final Learning Path

```text
                    YOUR JOURNEY

STEP 1
FastAPI Basics
      ↓
STEP 2
CRUD
      ↓
STEP 3
PostgreSQL
      ↓
STEP 4
SQLAlchemy ORM
      ↓
STEP 5
Multiple Tables
      ↓
STEP 6
Foreign Keys
      ↓
STEP 7
Relationships
      ↓
STEP 8
JOINs
      ↓
STEP 9
Reports
      ↓
STEP 10
Password Hashing
      ↓
STEP 11
Login
      ↓
STEP 12
JWT
      ↓
STEP 13
Protected Routes
      ↓
STEP 14
Authorization / Roles
```

### 🎯 Your current position

You have completed up to:

```text
✅ CRUD
✅ PostgreSQL
✅ SQLAlchemy ORM
✅ Relationships
✅ Foreign Keys
✅ JOINs
✅ Reports
✅ Password Hashing
✅ Registration
✅ Login
✅ JWT
✅ Swagger Authorization
✅ Protected `/students/profile`
```

The natural **next phase** is **Authorization with roles**:

```text
                    JWT
                     ↓
              get_current_user()
                     ↓
                 role?
                /      \
          student      admin
             ↓           ↓
       Student APIs   Admin APIs
```

That will complete the important difference between **Authentication** and **Authorization**.
