from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.student import Student
from schemas.student import StudentCreate

from security import get_current_user


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =========================
# GET ALL STUDENTS
# =========================

@router.get("/")
def get_students(
    con: Session = Depends(get_db)
):
    students = con.query(Student).all()

    return students


# =========================
# PROTECTED PROFILE
# IMPORTANT: BEFORE /{id}
# =========================

@router.get("/profile")
def student_profile(
    current_user = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user": current_user
    }


# =========================
# GET STUDENT BY ID
# =========================

@router.get("/{id}")
def get_student(
    id: int,
    con: Session = Depends(get_db)
):

    student = con.query(Student).filter(
        Student.student_id == id
    ).first()

    if student is None:
        return {
            "message": "Student not found"
        }

    return student


# =========================
# CREATE STUDENT
# =========================

@router.post("/")
def create_student(
    student: StudentCreate,
    con: Session = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        city=student.city
    )

    con.add(new_student)

    con.commit()

    con.refresh(new_student)

    return new_student


# =========================
# UPDATE STUDENT
# =========================

@router.put("/{id}")
def update_student(
    id: int,
    student: StudentCreate,
    con: Session = Depends(get_db)
):

    existing_student = con.query(Student).filter(
        Student.student_id == id
    ).first()

    if existing_student is None:
        return {
            "message": "Student not found"
        }

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email
    existing_student.city = student.city

    con.commit()

    con.refresh(existing_student)

    return existing_student


# =========================
# DELETE STUDENT
# =========================

@router.delete("/{id}")
def delete_student(
    id: int,
    con: Session = Depends(get_db)
):

    student = con.query(Student).filter(
        Student.student_id == id
    ).first()

    if student is None:
        return {
            "message": "Student not found"
        }

    con.delete(student)

    con.commit()

    return {
        "message": "Student deleted successfully"
    }