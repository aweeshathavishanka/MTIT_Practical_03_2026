from fastapi import FastAPI, HTTPException
from models import Student, StudentCreate, StudentUpdate
from service import StudentService
from typing import List

app = FastAPI()

student_service = StudentService()

@app.get("/")
def root():
    return {"message": "Student Service Running"}

@app.get("/api/students", response_model=List[Student])
def get_students():
    return student_service.get_all()

@app.get("/api/students/{student_id}")
def get_student(student_id: int):
    student = student_service.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404)
    return student

@app.post("/api/students")
def create_student(student: StudentCreate):
    return student_service.create(student)

@app.put("/api/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    return student_service.update(student_id, student)

@app.delete("/api/students/{student_id}")
def delete_student(student_id: int):
    return student_service.delete(student_id)