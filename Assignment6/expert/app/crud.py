from sqlalchemy.orm import Session

import models, schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()



def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(firstname=student.firstname, lastname=student.lastname, average = student.average, graduated = student.graduated)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_course(db: Session, course: schemas.CourseCreate, id:int):
    db_course = models.Course(name=course.name, unit=course.unit, owner_id=id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_course(db: Session, course_id :int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()



def create_student_course(db: Session, course: schemas.CourseCreate, student_id: int):
    db_course = models.Course(**course.dict(), owner_id=student_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course