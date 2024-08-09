from flask import Flask, jsonify
import requests




app = Flask(__name__)

khayam_url = "http://127.0.0.1:5002/today"
hafez_url = "http://127.0.0.1:5001/fal"


def call_khayam_hafez():
    response1 = requests.get(khayam_url)
    response2 = requests.get(hafez_url)
    return response1.json().get("datetimenow"), response2.json().get("fal")

  
@app.route("/", methods=["GET"])
def khayam_hafez():
    datetienow, fal = call_khayam_hafez()
    return jsonify({"today": str(datetienow), "fal" : str(fal)})
    

if __name__ == "__main__":
    app.run(port=8000)    

