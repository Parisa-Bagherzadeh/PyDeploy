from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from src.face_analysis import FaceAnalysis


app = FastAPI()
face_analysis = FaceAnalysis("models/det_10g.onnx", "models/genderage.onnx")



@app.get("/")
def index():
    return {"Hello" : "World"}

@app.post("/analyze-face/")
async def analyze_face(file: UploadFile = File(...)):
    image = await file.read()
    image_np_array = np.frombuffer(image, np.uint8)
    image_cv2 = cv2.imdecode(image_np_array, cv2.IMREAD_COLOR)
    output_image, genders, ages = face_analysis.detect_age_gender()

    result = {
        "genders": genders,
        "ages": ages
    }

    return JSONResponse(result) 
