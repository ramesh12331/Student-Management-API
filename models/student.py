from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    city = Column(String)

    marks = relationship(
        "Marks",
        back_populates="student"
    )