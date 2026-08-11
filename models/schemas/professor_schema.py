from pydantic import BaseModel, Field
from typing import Optional
class ProfessorCreate(BaseModel):
    name_first: str = Field(min_length=2,max_length=50)
    name_last: str = Field(min_length=2,max_length=50)
    code_personnel: str = Field(min_length=3,max_length=20)
    department: str = Field(min_length=2,max_length=80)
    

class ProfessorUpdate(BaseModel):
    name_first: Optional[str] = None
    name_last: Optional[str] = None
    code_personnel: Optional[str] = None
    department: Optional[str] = None
