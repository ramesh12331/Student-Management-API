from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from models import Student, Course, Marks

router = APIRouter (
    prefix = "/reports",
    tags = ["Reports"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/student-marks")
def get_student_marks(con:Session = Depends(get_db)):
    result = (con.query(Student.name, Course.course_name, Marks.marks).join(Marks, Student.student_id == Marks.student_id)).join(Course, Course.course_id == Marks.course_id).all()

    # return result

    return [
        {
            "student_name": row.name,
            "course_name": row.course_name,
            "marks": row.marks
        }
        for row in result
    ]

@router.get("/student/{student_id}")
def get_student_report(student_id : int, con:Session = Depends(get_db)):
    result = (
        con.query(
            Student.name, 
            Course.course_name, 
            Marks.marks
            )
            .join(
                Marks, 
                Student.student_id == Marks.student_id
            )
            .join(
            Course, 
            Course.course_id == Marks.mark_id
            )
            .filter(
            Student.student_id == student_id
            )
            .all()
        )

    if not result:
        return {
            "message": "Student or marks not found"
        }

    # return result

    return [
            {
                "student_name": row.name,
                "course_name": row.course_name,
                "marks": row.marks
            }
            for row in result
        ]

@router.get("/search/by-city")
def get_students_by_city(city:str, con:Session = Depends(get_db)):
    student = con.query(Student).filter(Student.city == city).all()

    return student

@router.get("/search/")
def get_marks_above(minimum:int, con:Session = Depends(get_db)):
    marks = con.query(Marks).filter(Marks.marks >= minimum).all()
    return marks

@router.get("/students-with-marks")
def get_students_with_marks(con:Session = Depends(get_db)):
    result = (con.query(Student.name, Marks.marks).join(Marks, Student.student_id == Marks.student_id).all())
    # return result

    return [
                {
                    "student_name": row.name,
                    "marks": row.marks
                }
                for row in result
            ]

@router.get("/course-students")
def get_course_students(con:Session = Depends(get_db)):
    result = (con.query(Course.course_name, Student.name, Marks.marks).join(Marks, Course.course_id == Marks.course_id).join(Student, Student.student_id == Marks.student_id).all())
    # return result

    return [
                    {
                        "course_name": row.course_name,
                        "student_name": row.name,
                        "marks": row.marks
                    }
                    for row in result
                ]

@router.get("/student-average/{student_id}")
def get_student_average(student_id : int, con:Session = Depends(get_db)):
    result = (
        con.query(
            Student.name,
            func.avg(Marks.marks).label("average_marks")
        )
        .join(
            Marks,
            Student.student_id == Marks.student_id
        )
        .filter(
            Student.student_id == student_id
        )
        .group_by(
            Student.name
        )
        .first()
    )

    if result is None:
         return {
            "message": "Student or marks not found"
        }

    return{
        "student" : result.name,
        "average_marks": round(
            float(result.average_marks),
            2
        )
    }