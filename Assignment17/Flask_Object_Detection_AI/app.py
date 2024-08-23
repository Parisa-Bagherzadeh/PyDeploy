from flask import Flask, request, jsonify
import numpy as np
import io
import base64
from PIL import Image
from src.object_detection import YOLOv8


app = Flask("Object Detection")
object_detector = YOLOv8("models/yolov8n.onnx")


@app.route("/", methods=["GET"])
def index():
    return {"Hello": "World"}

@app.route("/detect", methods=["POST"])
def detect():
    image = request.files["file"]
    image_pil = Image.open(image.stream)
    image_np_array = np.array(image_pil)
    output_image, labels = object_detector(image_np_array)

    result = {

        "labels": labels
    }

    return jsonify(result)

