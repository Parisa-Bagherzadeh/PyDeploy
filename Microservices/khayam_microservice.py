from flask import Flask, jsonify
from khayyam import *


app = Flask(__name__)

@app.route("/today", methods=["GET"])
def fal_hafez():
    datetimenow = str(JalaliDatetime.now().strftime('%C'))
    return jsonify({"today" : datetimenow})

if __name__ == "__main__":
    app.run(port=5002)
