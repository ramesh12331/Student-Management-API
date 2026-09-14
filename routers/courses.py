from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.course import Course
from schemas.course import CourseCreate

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_courses(con:Session = Depends(get_db)):
    courses = con.query(Course).all()
    return courses

@router.get("/{id}")
def get_course(id:int, con:Session = Depends(get_db)):
    course = con.query(Course).filter(Course.course_id == id).first()

    if course is None:
        return{
            "message": "Course not found"
        }
    return course

@router.post("/")
def create_courses(course:CourseCreate, con:Session = Depends(get_db)):
    new_course = Course(
        course_name = course.course_name,
        duration = course.duration
    )

    con.add(new_course)
    con.commit()
    con.refresh(new_course)

    return new_course

@router.put("/{id}")
def update_course(id:int, course:CourseCreate, con:Session = Depends(get_db)):
    existing_course = con.query(Course).filter(Course.course_id == id).first()

    if existing_course is None:
        return{
            "message" : "Course not found"
        }

    existing_course.course_name = course.course_name
    existing_course.duration = course.duration

    con.commit()
    con.refresh(existing_course)

    return existing_course

@router.delete("/{id}")
def delete_course(id:int, con:Session = Depends(get_db)):
    course = con.query(Course).filter(Course.course_id == id).first()
    if course is None:
        return{
            "message" : "Course not found"
        }
    con.delete(course)
    con.commit()

    return{
        "message": "Course deleted successfully"
    }


