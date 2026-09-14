from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    duration = Column(Integer)

    marks = relationship(
        "Marks",
        back_populates="course"
    )