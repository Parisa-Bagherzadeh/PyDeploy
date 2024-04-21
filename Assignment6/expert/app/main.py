from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    yield db
    db.close()


@app.get("/")
def read_root():
   return{"message" : "API University System. This API allows you to manage students and courses within a university system.With this API, you can perform CRUD (Create, Read, Update, Delete) operations on students and courses, enabling you to maintain accurate records of enrolled students and available courses."}


@app.get("/students/", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.create_student(db=db, student=student)
    return db_student




@app.put("/students", response_model=schemas.Student)
def update_student(student_id: int,student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(student_id=student_id, db=db, student=student)
    return db_student

@app.delete("/students/{student_id}")
def delete_student_db(student_id:int, db:Session = Depends(get_db)):
    db_student = crud.delete_student(db=db, student_id=student_id)
    return db_student




@app.post("/courses/", response_model=schemas.Course)
def create_course(id : int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.create_course(db=db, course=course,id=id)
    return db_course


@app.get("/courses/", response_model=schemas.Course)
def read_course(course_id : int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course

@app.put("/courses", response_model=schemas.Course)
def update_course(course_id: int,course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.update_course(course_id=course_id, db=db, course=course)
    return db_course


@app.delete("/courses/{course_id}")
def delete_course_db(course_id:int, db:Session = Depends(get_db)):
    db_course = crud.delete_course(db=db, course_id=course_id)
    return db_course



