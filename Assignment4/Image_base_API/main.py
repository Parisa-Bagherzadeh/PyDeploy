from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis
import cv2
import numpy as np
import io



app = FastAPI()

@app.get("/")
def root():
    return "Hello, this is an Image based API :)"

@app.post("/deepface")
async def deep_face(input_file : UploadFile = File(None)):
    
    THRESHOLD = 25

    face = FaceAnalysis(name = "buffalo_s", providers = ["CPUExecutionProvider"])
    face.prepare(ctx_id = 0, det_size = (640, 640))

    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code = 415, detail = "Unsupported file")
    
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype = np.uint8)
    input_image = cv2.imdecode(np_array, cv2.COLOR_BGR2RGB)

    result_image = input_image.copy()

    results = face.get(input_image)
    face_bank = np.load("face_bank.npy", allow_pickle=True)
    result_image = input_image.copy()

    for result in results:
        cv2.rectangle(result_image, (int(result.bbox[0]), 
                                    int(result.bbox[1])), 
                                    (int(result.bbox[2]), 
                                    int(result.bbox[3])),(0, 0, 255),4)    

        for person in face_bank:
            face_bank_person_embedding = person["embedding"]
            new_person_embedding = result["embedding"]

            distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))

            if distance < THRESHOLD:
                cv2.putText(result_image, person["name"],
                (int(result.bbox[0]) - 40, int(result.bbox[1] - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0),3, cv2.LINE_AA)
                break

        else:
            cv2.putText(result_image, "Unknown",
            (int(result.bbox[0]) - 40, int(result.bbox[1])),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3,cv2.LINE_AA)

    cv2.imwrite("output/result.jpg",result_image)
    _, encoded_image = cv2.imencode(".jpg", result_image)
    image_bytes = encoded_image.tobytes()
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
            
    