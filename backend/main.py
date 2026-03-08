from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import users, tasks

# Create the FastAPI app FIRST
app = FastAPI(
    title="Task Manager",
    description="Backend of the Task Manager",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])


@app.get("/")
def root():
    return {"message": "Hello, welcome to the application"}