from flask import Flask, render_template, request


app = Flask("Test Project")

@app.route("/")
def my_root():
#    return "<p> Hello Flask! </p>"
    name = "Parisa"
    return render_template("index.html", name=name, x=10)
   
#    name = "Sajjad"
# @app.route("/download")
# def download():
#     media = ["image", "music", "film"]
#     return render_template("download.html")
# @app.route("/download")
# def download():
#     media = ["image", "music", "film"]
#     return render_template("download.html")
#    return render_template("index.html", name=name, x=10)

@app.route("/download")
def download():
    media = ["image", "music", "film"]
    return render_template("download.html", media=media)
                        
# def download():
#     media = ["image", "music", "film"]
#     return render_template("download.html")


@app.route("/", methods=["GET"])
def my_information():
    my_info = {"firstname": "Parisa", "email": "parisa.bagherzadeh@gmail.com"}
    return my_info

@app.route("/blog",methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "This is the GET method"
    elif request.method == "POST":
        return "This is the POST method"
