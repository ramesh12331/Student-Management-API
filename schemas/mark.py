from pydantic import BaseModel, Field

class MarksCreate(BaseModel):
    student_id : int = Field(gt=0)
    course_id : int = Field(gt=0)
    marks : int = Field(gt=0, le=100)