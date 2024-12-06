import time
import random
import requests
from fastapi import FastAPI
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "👋🏻"}


@app.post("/auth/gesture")
async def gesture():

    base_options = python.BaseOptions(model_asset_path='gesture_recognizer/gesture_recognizer.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)

    images = []
    results = []
    image_file_name = "test_images/pointing_up"
    # STEP 3: Load the input image.
    image = mp.Image.create_from_file(image_file_name)

# STEP 4: Recognize gestures in the input image.
    recognition_result = recognizer.recognize(image)

    # STEP 5: Process the result. In this case, visualize it.
    images.append(image)
    top_gesture = recognition_result.gestures[0][0]
    hand_landmarks = recognition_result.hand_landmarks
    results.append((top_gesture, hand_landmarks))

    print(top_gesture)

    # time.sleep(20)
    # result = random.choice(["👍🏻","👎🏻", "✌🏻"])
    # return {"result": result}