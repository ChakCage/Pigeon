from pydantic import BaseModel

class TaskSchema(BaseModel):
    id : int
    title: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str