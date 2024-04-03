import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis


def main():

    app = FaceAnalysis(name = "buffalo_s", providers = ["CPUExecutionProvider"])
    app.prepare(ctx_id = 0, det_size = (640, 640))

    face_bank_path = './face_bank'

    face_bank = []

    for person_name in os.listdir(face_bank_path):
        file_path = os.path.join(face_bank_path, person_name)
        if os.path.isdir(file_path):
            for image_name in os.listdir(file_path):
                image_path = os.path.join(file_path, image_name)
                print(image_path)

                image = cv2.imread(image_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                result = app.get(image)

                if len(result) > 1:
                    print("Warning : more than one face detected")
                    continue

                embedding = result[0]["embedding"]
                mydict = {"name": person_name, "embedding": embedding}
                face_bank.append(mydict)

    np.save("face_bank.npy", face_bank)


if __name__ == "__mian__":
    main()