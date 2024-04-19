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
    return "Hey! Welcome :)"



@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.create_student(db=db, student=student)
    return db_student


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student




@app.post("/courses/", response_model=schemas.Course)
def create_course(id : int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.create_course(db=db, course=course,id=id)
    return db_course


@app.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id : int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course

