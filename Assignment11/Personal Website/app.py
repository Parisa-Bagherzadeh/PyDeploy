from flask import Flask, render_template


app = Flask("Personal_Website")

@app.route("/")
def root():
    return render_template("index.html")
