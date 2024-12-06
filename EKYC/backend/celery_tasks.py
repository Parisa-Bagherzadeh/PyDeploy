import time
import random
import requests
from celery import Celery


celery_app = Celery(
    'tasks', 
    broker='redis://localhost:6379',
    backend='redis://localhost:6379'
)

@celery_app.task
def face_task(face_data: bytes):
    time.sleep(20)
    result = random.choice([True, False])
    return {"status": "completed",
            "result": result}



@celery_app.task
def speech_task(speech_data: bytes):
    time.sleep(5)
    result = random.choice([True, False])
    return {"status": "completed",
            "result": result}



@celery_app.task
def gesture_task(gesture_data: bytes):
    response = requests.post("http://127.0.0.1:8080/auth/gesture")
    result = response.json()
    return {"status": "completed",
            "result": result}