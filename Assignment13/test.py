from deepface import DeepFace

objs = DeepFace.analyze(
    img_path = "parisa.jpg",
    actions= ['age']
)

print(objs)