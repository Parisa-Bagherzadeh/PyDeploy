from fastapi import FastAPI,UploadFile
from celery_tasks import celery_app, face_task, speech_task, gesture_task


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/auth/face")
async def face(image_file: UploadFile):
    image = await image_file.read()
    task = face_task.delay(image)
    return {"task_id": task.id,
            "status": task.status}


@app.post("/speech")
async def speech(voice_file: UploadFile):
    voice = await voice_file.read()
    task = speech_task.delay(voice)
    return {"task_id": task.id,
            "status": task.status}

@app.post("/gesture")
async def gesture(image_file: UploadFile):
    image = await image_file.read()
    task = gesture_task.delay(image)
    return { "task_id": task.id, 
            "status": task.status}


@app.get("/check-task")
def check_task(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {result.state}