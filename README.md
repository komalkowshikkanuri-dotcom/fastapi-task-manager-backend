# Task Manager Backend API (FastAPI)

This is a backend API for a task management system built with **FastAPI**.  
Users can register, log in, and manage their tasks securely using **JWT authentication**.

---

## Features

- User signup
- User login with JWT authentication
- Password hashing using bcrypt
- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Protected routes
- SQLite database
- Swagger API documentation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)

---

## Project Structure


backend/
│
├── routes/
│ ├── tasks.py
│ └── users.py
│
├── auth.py
├── database.py
├── main.py
├── models.py
└── schemas.py


---

## Installation

Clone the repository


git clone https://github.com/komalkowshikkanuri-dotcom/fastapi-task-manager-backend


Install dependencies


pip install -r requirements.txt


Run the server


uvicorn backend.main:app --reload


---

## API Documentation

After running the server open:


http://127.0.0.1:8000/docs


---

## Author

Built by **Komal Kowshik**