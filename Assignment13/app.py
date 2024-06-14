import os
import bcrypt
from flask import Flask, render_template, request, redirect,session,url_for
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel
from datetime import datetime
from ultralytics import YOLO
# from deepface import DeepFace
import cv2

app = Flask("app")
app.config["UPLOAD_FOLDER"] = './uploads'
app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg'}

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field()
    password: str = Field()
    firstname: str = Field()
    lastname: str = Field()
    country: str = Field()
    city: str = Field()
    email: str = Field()
    age:int = Field()
    join_time: str = Field()
  


engine = create_engine('sqlite:///./database.db', echo=True)
SQLModel.metadata.create_all(engine)

# PyDantic models for request validation 
class RegisterModel(BaseModel):
    username: str
    password: str
    confirm_password: str
    firstname: str
    lastname: str
    country: str
    city: str
    email: str
    age: int
    join_time : str

class LoginModel(BaseModel):
    username: str
    password: str


# def auth(email,password):
#     if email == "parisa@gmail.com" and password == "1234":
#         return True
#     else:
#         return False
    
def allowed_file(filename):
    format = filename.split('.')[-1]
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
        try:
            login_model = LoginModel(
            username = request.form["username"],
            password = bcrypt.hashpw(request.form["password"].encode('utf-8'),bcrypt.gensalt())
            
            )
            
        except:
            print("Type error")
            return redirect(url_for("login"))
        
        with Session(engine) as db_session:
            print("-----------------------------------------")
            print(login_model.password)
            statement = select(User).where(User.username == login_model.username).where(User.password == login_model.password)
            result = db_session.exec(statement).first()

        if result:
            print("Welcome, you are logged in")
            return redirect(url_for("upload"))
        else:
            print("Username or password is incorrect")
            return redirect(url_for("login"))
        

@app.route("/register", methods=["GET", "POST"])        
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        try:
            register_data = RegisterModel(
            city = request.form["city"], 
            username = request.form["username"], 
            password = request.form["password"],
            confirm_password = request.form["confirm_password"],
            firstname = request.form["firstname"],
            lastname = request.form["lastname"],
            country = request.form["country"],
            age = request.form["age"],
            email = request.form["email"],
            join_time = datetime.today().strftime('%Y-%m-%d')

            )
        except:    
            print("Type Error")   
            return redirect(url_for("register"))

        with Session(engine) as db_session:
            statement = select(User).where(User.username == register_data.username)    
            result = db_session.exec(statement).first()

        if not result:
            if register_data.password == register_data.confirm_password:
        
                with Session(engine) as db_session:
                    user = User(
                        username = register_data.username,
                        city = register_data.city,
                        password = bcrypt.hashpw(register_data.password.encode('utf-8'),bcrypt.gensalt()),
                        firstname = register_data.firstname,
                        lastname = register_data.lastname,
                        country = register_data.country,
                        age = register_data.age,
                        email = register_data.email, 
                        join_time = register_data.join_time
                    )
                    db_session.add(user)
                    db_session.commit()

                print("Registered done successfuly")  
                return redirect(url_for("login"))  
            else:
                print("Different passwords!")
                return redirect(url_for("register"))
        else:
            print("Usrename already exist, try another username")  
            return redirect(url_for("register"))            



@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        

        my_image = request.files['image']
        if my_image.filename == "":
            return redirect(url_for("upload"))
        else:
            
            if allowed_file(my_image.filename):
                print(my_image.filename)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                image = cv2.imread(save_path)
                model = YOLO("yolov8n-cls.pt")

                results = model.predict(image)
              
                
                return render_template("result.html", result=results)

            else:
                print("You are allowed to upload just images") 
                return redirect(url_for("upload"))   
                
            
        
 


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