from pydantic import BaseModel, Field

class CourseCreate(BaseModel):
    course_name : str = Field(min_length=2)
    duration : int = Field(gt=0)