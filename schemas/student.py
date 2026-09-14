from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name : str = Field(min_length=2)
    age : int = Field(gt=0, lt=100)
    email : str
    city : str = Field(min_length=2)