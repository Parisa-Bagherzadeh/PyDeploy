import os
import bcrypt

from flask import Flask, flash, render_template, request, redirect,session as flask_session, url_for
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel
from datetime import datetime, timedelta

# from ultralytics import YOLO
# from deepface import DeepFace

import cv2



def relative_date(past_date):
    past_date = (datetime.strptime(past_date, "%Y-%m-%d %H:%M:%S"))
    now = datetime.now()
    delta = now - past_date

    if delta.days >= 365:
        years = delta.days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif delta.days >= 30:
        months = delta.days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif delta.days >= 7:
        weeks = delta.days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif delta.days > 0:
        return f"{delta.days} day{'s' if delta.days > 1 else ''} ago"
    elif delta.seconds >= 3600:
        hours = delta.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif delta.seconds >= 60:
        minutes = delta.seconds // 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "just now"



app = Flask("app")
app.secret_key = "secret_key"
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
  
  
class Comment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    user_id: int = Field(foreign_key="user.id")

# engine = create_engine('sqlite:///./database.db', echo=True)
# SQLModel.metadata.create_all(engine)

# DATABASE_URL = "postgresql://parisa:110@localhost:5432/database"
DATABASE_URL = "postgresql://parisa:110@some-postgres:5432/postgres"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)

#docker run --network my_network --name database -e POSTGRES_PASSWORD=110 -e POSTGRES_USER=parisa -e POSTGRES_DB=postgressql
#-d postgres

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


def allowed_file(filename):
    format = filename.split('.')[-1]
    if format in("jpeg", "png", "jpg"):
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
            password = request.form["password"])
            
        except:
            flash("Type error", "warning")
            return redirect(url_for("login"))
        
        with Session(engine) as db_session:
            statement = select(User).where(User.username == login_model.username)
            user = db_session.exec(statement).first()
            
        if user:
            password_byte = login_model.password.encode("utf-8")
            # if bcrypt.checkpw(password_byte, bytes(user.password, "utf-8")):
            if bcrypt.checkpw(password_byte, user.password):
                flash("Welcome, you are logged in", "success")
                flask_session["user_id"] = user.id
                return redirect(url_for("profile"))
               
            else:
                flash("Password is incorrect", "danger")
                return redirect(url_for("login"))
        else:
            flash("Username is incorrect", "danger")
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
            join_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
             
            # join_time = datetime.now()

            )
        except:    
            flash("Type Error")   
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
                    db_session.refresh(user)
                flash("Registered done successfuly")  
                engine.dispose()
                return redirect(url_for("login"))  
            else:
                flash("Different passwords!")
                return redirect(url_for("register"))
        else:
            flash("Usrename already exist, try another username")  
            return redirect(url_for("register"))            


@app.route("/object-detection", methods=["GET", "POST"])
def upload():
    if flask_session.get('user_id'):
        if request.method == "GET":
            with Session(engine) as db_session:
                statement = select(Comment)
                comments = list(db_session.exec(statement))
                return render_template("object_detection.html", comments=comments)  

        elif request.method == "POST":
            my_image = request.files['image']
            if my_image.filename == "":
                return redirect(url_for("object_detection"))
            else:
                if allowed_file(my_image.filename):
                    flash(my_image.filename)
                    save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                    image = cv2.imread(save_path)
                    print(image)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    model = YOLO("yolov8n.pt")
                    results = model.predict(save=True, source=image)
                    for result in results:
                        boxes = result.boxes
                        for box in boxes:
                            coor = box.xyxy.tolist()
                            x = int(coor[0][0])
                            y = int(coor[0][1])
                            w = int(coor[0][2]) - int(coor[0][0])
                            h = int(coor[0][3]) - int(coor[0][1])
                            new_image = image.copy()
                            image_box = cv2.rectangle(new_image,(x, y), (w, h),(255, 0, 0), 2)
                            cv2.imshow("Image", image_box)

                else:
                    flash("You are allowed to upload just images") 
                    return redirect(url_for("object_detection"))   
    else:
        return redirect(url_for("index"))                   
                
        

@app.route("/bmr", methods=["GET", "POST"])
def cal_bmr():
    if request.method == "GET":
        return render_template("bmr.html")
    else:
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        age = float(request.form["age"])
        gender = str(request.form["gender"])
        if gender.lower() == "female":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        elif gender.lower() == "male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5 
        else:
            return redirect(url_for("cal_bmr"))
    return f"🧮 Your BMR is {bmr}"   


@app.route("/profile") 
def profile():
    return render_template("profile.html")    
 


@app.route("/mind-reader", methods=["GET", "POST"])
def mind_reader():
    if request.method == "POST":
        x = request.form["number"]
        return redirect(url_for("mind_reader_result", number=x))
    return render_template("mind-reader.html")


@app.route("/mind-reader/result")
def mind_reader_result():
    y = request.args.get("number")
    return render_template("mind-reader-result.html", number=y)


@app.route("/pose-detection")
def pose_detection():
    if flask_session.get('user_id'):
        return render_template("pose-detection.html")
    else:
        flash("You must login first")
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    if flask_session.get('user_id'):
        flask_session.pop("user_id")
        return redirect(url_for("index"))
    else:
        return render_template("index.html")
        

@app.route("/admin")
def admin():
    user_id = flask_session.get('user_id')
    # role = flask_session.get('role')
    # if not user_id or role != "Admin":
    if not user_id:
        return redirect(url_for('login'))
    else:
        with Session(engine) as db_session:
            statement_user = select(User)
            users = list(db_session.exec(statement_user))

            statement_comment = select(Comment)
            comments = list(db_session.exec(statement_comment))

        for user in users:
            user.join_time = relative_date(user.join_time) 

        return render_template("admin.html", users=users, comments=comments)




@app.route("/add-new-comment", methods=["POST"])
def add_new_comment():
    comment = request.form["comment"]
    with Session(engine) as db_session:
        new_comment = Comment(
            user_id= flask_session.get("user_id"),
            content=comment
        )
        db_session.add(new_comment)
        db_session.commit()

    return render_template("object_detection.html")    


@app.route("/registered_users")
def registered_users():
    return render_template("registered_users.html")  



# @app.route("/object-detection")
# def show_comments():
#     with Session(engine) as db_session:
#         statement = select(Comment)
#         comments = list(db_session.exec(statement))
#     return render_template("object-detection.html", comments=comments)    


