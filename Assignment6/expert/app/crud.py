from sqlalchemy.orm import Session
from fastapi import  HTTPException
import models, schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()



def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(firstname=student.firstname, lastname=student.lastname, average = student.average, graduated = student.graduated)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(student_id:int, db: Session, student: schemas.StudentCreate):
    db_student =  db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db_student.firstname = student.firstname
    db_student.lastname = student.lastname
    db_student.average = student.average
    db_student.graduated = student.graduated
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db:Session, student_id:int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return "Student removed"



def get_course(db: Session, course_id :int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def create_course(db: Session, course: schemas.CourseCreate, id:int):
    db_course = models.Course(name=course.name, unit=course.unit, owner_id=id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(course_id:int, db: Session, course: schemas.StudentCreate):
    db_course =  db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

def delete_course(db:Session, course_id:int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return "Course removed"





