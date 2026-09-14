from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Student, Course, Marks
from schemas.mark import MarksCreate

router = APIRouter(
    prefix="/marks",
    tags=["Marks"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_marks(con : Session = Depends(get_db)):
    marks = con.query(Marks).all()
    return marks

@router.get("/{id}")
def get_mark(id:int, con:Session = Depends(get_db)):
    mark = con.query(Marks).filter(Marks.mark_id == id).first()

    if mark is None:
        return{
            "message" : "Marks not found"
        }
    return mark

@router.post("/")
def creat_mark(mark:MarksCreate, con:Session = Depends(get_db)):

    student = con.query(Student).filter(Student.student_id == mark.student_id).first()

    if student is None:
        return{
            "message" : "Student not found"
        }

    course = con.query(Course).filter(Course.course_id == mark.course_id).first()

    if course is None:
        return {
            "message": "Course not found"
        }
    
    new_mark = Marks(
        student_id = mark.student_id,
        course_id = mark.course_id,
        marks = mark.marks
    )

    con.add(new_mark)
    con.commit()
    con.refresh(new_mark)

    return new_mark

@router.put("/{id}")
def update_mark(id:int, mark:MarksCreate, con:Session = Depends(get_db)):
    existing_mark = con.query(Marks).filter(Marks.mark_id == id).first()

    if existing_mark is None:
        return {
            "message": "Mark not found"
        }

    existing_mark.student_id = mark.student_id
    existing_mark.course_id = mark.course_id
    existing_mark.marks = mark.marks

    con.commit()
    con.refresh(existing_mark)
    return existing_mark

@router.delete("/{id}")
def delete_mark(id:int, con:Session = Depends(get_db)):
    mark = con.query(Marks).filter(Marks.mark_id == id).first()
    if mark is None:
        return {
            "message": "Mark not found"
        }
    con.delete(mark)
    con.commit()

    return {
        "message": "Mark deleted successfully"
    }
    
    