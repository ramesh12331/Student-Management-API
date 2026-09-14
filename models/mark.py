from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Marks(Base):
    __tablename__ = "marks"

    mark_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    marks = Column(Integer)

    student = relationship(
        "Student",
        back_populates="marks"
    )

    course = relationship(
        "Course",
        back_populates="marks"
    )