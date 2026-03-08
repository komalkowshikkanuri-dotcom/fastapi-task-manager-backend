from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class TaskCreate(BaseModel):
    description: str


class TaskUpdate(BaseModel):
    description: str
    completed: bool


class TaskResponse(BaseModel):
    id: int
    description: str
    completed: bool

    class Config:
        from_attributes = True