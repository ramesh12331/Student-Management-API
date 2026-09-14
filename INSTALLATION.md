Absolutely. Here is the **complete installation and running process from zero to successfully running your Student Management API**, in beginner-friendly order.

# 🚀 Student Management API — Installation to Run

## 1. Check Python

Open **Command Prompt / PowerShell**:

```bash
python --version
```

You should see something like:

```text
Python 3.x.x
```

Also check pip:

```bash
pip --version
```

---

# 2. Create Project Folder

Choose a location and create your project:

```bash
mkdir student_management_api
cd student_management_api
```

Your terminal should now be inside:

```text
student_management_api
```

---

# 3. Create Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

This creates:

```text
student_management_api/
└── venv/
```

### Why?

The virtual environment keeps your project's Python packages separate from other projects.

---

# 4. Activate Virtual Environment

On **Windows**:

```bash
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

For example:

```text
(venv) C:\Users\...\student_management_api>
```

---

# 5. Upgrade pip

Recommended:

```bash
python -m pip install --upgrade pip
```

---

# 6. Install Main Packages

Install the packages required by your project:

```bash
pip install fastapi uvicorn pydantic SQLAlchemy psycopg2-binary passlib python-jose[cryptography] python-multipart
```

These packages provide:

```text
fastapi              → API
uvicorn              → Server
pydantic             → Validation
SQLAlchemy           → ORM
psycopg2-binary      → PostgreSQL connection
passlib              → Password hashing
python-jose          → JWT
python-multipart     → OAuth2 form login
cryptography         → Security support
```

---

# 7. Create requirements.txt

After installing:

```bash
pip freeze > requirements.txt
```

Now your project has:

```text
student_management_api/
├── requirements.txt
└── venv/
```

Later, you can install the same environment using:

```bash
pip install -r requirements.txt
```

---

# 8. Install PostgreSQL

You need **PostgreSQL** because your API stores:

```text
Students
Courses
Marks
Users
```

inside PostgreSQL.

During PostgreSQL installation, remember the password you create for the PostgreSQL user.

For example:

```text
Username: postgres
Password: your_password
Port: 5432
```

---

# 9. Create Database

Open **pgAdmin** or PostgreSQL's SQL tool.

Create a database:

```sql
CREATE DATABASE fastapi_db;
```

Your database is now:

```text
PostgreSQL
    ↓
fastapi_db
```

---

# 10. Configure database.py

Your `database.py` should contain your PostgreSQL connection.

Example:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

### Important

Replace:

```text
YOUR_PASSWORD
```

with your actual PostgreSQL password.

For example:

```python
DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"
```

---

# 11. Create Project Structure

Your final project should look like:

```text
student_management_api/
│
├── venv/
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

# 12. Important `__init__.py` Files

Create these three files:

```text
models/__init__.py
schemas/__init__.py
routers/__init__.py
```

They can initially be empty.

---

# 13. Create Your Models

Your database models represent PostgreSQL tables:

```text
Student
   ↓
students table

Course
   ↓
courses table

Mark
   ↓
marks table

User
   ↓
users table
```

You already have the model files:

```text
models/student.py
models/course.py
models/mark.py
models/user.py
```

---

# 14. Create Your Schemas

Schemas define the data accepted by the API:

```text
schemas/
├── student.py
├── course.py
├── mark.py
└── user.py
```

Pydantic handles validation.

For example:

```python
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    city: str
```

---

# 15. Create Security

Your `security.py` handles:

```text
Password Hashing
       +
JWT Token
       +
JWT Verification
```

The important packages are:

```python
from passlib.context import CryptContext
from jose import jwt
```

---

# 16. Create Routers

Your API is divided into separate routers:

```text
routers/
│
├── students.py
├── courses.py
├── marks.py
├── reports.py
└── auth.py
```

This keeps the project organized.

For example:

```text
students.py
    ↓
/students/

courses.py
    ↓
/courses/

marks.py
    ↓
/marks/

auth.py
    ↓
/auth/
```

---

# 17. Configure `main.py`

Your `main.py` connects everything together.

The important part is:

```python
from fastapi import FastAPI

from database import Base, engine

from models.student import Student
from models.course import Course
from models.mark import Mark
from models.user import User

from routers import students
from routers import courses
from routers import marks
from routers import reports
from routers import auth

app = FastAPI(
    title="Student Management API"
)

Base.metadata.create_all(bind=engine)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(marks.router)
app.include_router(reports.router)
app.include_router(auth.router)
```

---

# 18. Start the FastAPI Server

Make sure you are inside:

```text
student_management_api
```

and the virtual environment is active:

```text
(venv)
```

Run:

```bash
uvicorn main:app --reload
```

You should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

🎉 Your API is running!

---

# 19. Open Swagger UI

Open your browser:

```text
http://127.0.0.1:8000/docs
```

You will see:

```text
Student Management API
```

Swagger gives you an interactive interface for testing your endpoints.

---

# 20. Test Home Endpoint

In Swagger:

```text
GET /
```

Click:

```text
Try it out
```

then:

```text
Execute
```

Expected:

```json
{
    "message": "Student Management API is Working"
}
```

---

# 21. Test Registration

Go to:

```text
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

Click:

```text
Execute
```

Expected:

```json
{
    "message": "User registered successfully",
    "user_id": 1,
    "username": "ravi"
}
```

The password stored in PostgreSQL will be **hashed**, not plain text.

---

# 22. Test Login

Because we use:

```python
OAuth2PasswordRequestForm
```

login uses **form data**, not JSON.

Go to:

```text
POST /auth/login
```

Click:

```text
Try it out
```

Enter:

```text
username: ravi
password: python123
```

Then execute.

Expected:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

---

# 23. Authorize Swagger

At the top of Swagger, click:

```text
🔒 Authorize
```

For the OAuth2 login flow, enter your username/password when Swagger asks for them.

Use:

```text
username: ravi
password: python123
```

Leave:

```text
client_id: blank
client_secret: blank
```

Then click:

```text
Authorize
```

---

# 24. Test Protected Endpoint

Now go to:

```text
GET /students/profile
```

This endpoint requires authentication.

Click:

```text
Try it out
```

then:

```text
Execute
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

🎉 JWT authentication is working.

---

# 25. Test Student CRUD

### Create Student

```text
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

### Get All Students

```text
GET /students/
```

### Get One Student

```text
GET /students/1
```

### Update Student

```text
PUT /students/1
```

Example:

```json
{
    "name": "Ravi Kumar Updated",
    "age": 22,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

### Delete Student

```text
DELETE /students/1
```

---

# 26. Test Course CRUD

Create:

```text
POST /courses/
```

Example:

```json
{
    "course_name": "Python",
    "duration": 6
}
```

Then test:

```text
GET /courses/
GET /courses/1
PUT /courses/1
DELETE /courses/1
```

---

# 27. Add Marks

Example:

```text
POST /marks/
```

```json
{
    "student_id": 1,
    "course_id": 1,
    "marks": 85
}
```

You can then test:

```text
GET /marks/
GET /marks/1
PUT /marks/1
DELETE /marks/1
```

---

# 28. Test Reports

Your report endpoints include:

```text
GET /reports/student-marks

GET /reports/student/{student_id}

GET /reports/search/by-city

GET /reports/search/

GET /reports/students-with-marks

GET /reports/course-students

GET /reports/student-average/{student_id}
```

For example:

```text
GET /reports/student-average/1
```

can calculate the student's average marks.

---

# 🔄 29. Complete Project Flow

The entire application works like this:

```text
                 CLIENT
            Swagger / Postman
                    │
                    ↓
                FastAPI
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
    Students     Courses       Auth
        │           │           │
        ↓           ↓           ↓
      Router       Router     Router
        │           │           │
        └───────────┼───────────┘
                    ↓
                SQLAlchemy
                    │
                    ↓
                PostgreSQL
```

Authentication adds:

```text
User
 ↓
Register
 ↓
Passlib
 ↓
Hashed Password
 ↓
Login
 ↓
python-jose
 ↓
JWT
 ↓
Protected Endpoint
```

---

# 🧪 30. Final Running Checklist

Every time you want to run the project:

### Step 1 — Open terminal

```bash
cd student_management_api
```

### Step 2 — Activate environment

```bash
venv\Scripts\activate
```

### Step 3 — Start server

```bash
uvicorn main:app --reload
```

### Step 4 — Open Swagger

```text
http://127.0.0.1:8000/docs
```

### Step 5 — Test

```text
GET /
    ↓
POST /auth/register
    ↓
POST /auth/login
    ↓
Authorize 🔒
    ↓
GET /students/profile
    ↓
Student CRUD
    ↓
Course CRUD
    ↓
Marks CRUD
    ↓
Reports
```

# ⭐ From Zero to Run — Commands Only

If everything is being created from scratch on Windows:

```bash
mkdir student_management_api
cd student_management_api
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install fastapi uvicorn pydantic SQLAlchemy psycopg2-binary passlib python-jose[cryptography] python-multipart
pip freeze > requirements.txt
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

**Important:** PostgreSQL must be installed and the `fastapi_db` database must exist before starting the API. Your `DATABASE_URL` must also contain the correct PostgreSQL username/password.
