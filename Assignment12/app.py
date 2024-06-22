import os
from flask import Flask, render_template, request, redirect,session,url_for
# from deepface import DeepFace
import cv2

app = Flask("app")
app.config["UPLOAD_FOLDER"] = './uploads'
app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg'}


def auth(email,password):
    if email == "parisa@gmail.com" and password == "1234":
        return True
    else:
        return False
    
def allowed_file(filename):
    format = filename.split('.')[1]
    if format == "jpg" or format == "png" or format == "jpeg":
        return True
    else:
        return False

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        result = auth(email,password)

        if result:
            #upload
            return redirect(url_for("upload"))
        else:
            #login
            return redirect(url_for("login"))


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        my_image = request.files['image']
        if my_image.filename == "":
            return redirect(url_for("upload"))
        else:
            if my_image and allowed_file(my_image.filename):
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                my_image.save(save_path)
                result = DeepFace.analyze(
                img_path = save_path,
                actions= ['age']
            )
            

            age = result[0]['age']
            print(age)
            
        return render_template("result.html", age=result[0]['age'])
 


@app.route("/bmr", methods=["GET", "POST"])
def cal_bmr():

    if request.method == "GET":
        return render_template("bmr.html")
    else:
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        age = float(request.form["age"])
        gender = str(request.form["gender"])


        if gender == "female":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        elif gender == "male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5 
        else:
            return redirect(url_for("cal_bmr"))
        
    return f"🧮 Your BMR is {bmr}"        
