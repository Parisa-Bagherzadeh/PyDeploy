import numpy as np
from PIL import Image
import cv2
import onnxruntime as ort


onnx_session = ort.InferenceSession(
    "genderage.onnx",
    providers=["CPUExecutionProvider"]
)

input_name = onnx_session.get_inputs()[0].name
output_name = onnx_session.get_outputs()[0].name
input_shape = onnx_session.get_inputs()[0].shape
output_shape = onnx_session.get_outputs()[0].shape

print("Input name:",input_name, ", Output name:" ,output_name, 
      ", Input shape:",input_shape, ", Output shape:", output_shape)

image = Image.open("me.jpg")
image = image.resize((96, 96))

image = np.array(image).astype(np.float32)
image = np.expand_dims(image, axis=0)
image = np.transpose(image, (0, 3, 1, 2))
onnx_input = image


pred = onnx_session.run(
    [output_name],
    {input_name: onnx_input}
)

print(pred)