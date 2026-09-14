from fastapi import FastAPI
from database import Base, engine

from models import student, course
from models.user import User

from routers import students, courses, marks, reports, auth

app = FastAPI(
    title="Student Management API"
)

# Create database tables

Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(marks.router)
app.include_router(reports.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return{
        "message" : "Student Management API is Working"
    }


