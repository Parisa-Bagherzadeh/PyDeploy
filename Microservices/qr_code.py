from flask import Flask, send_file
import qrcode
import requests


app = Flask(__name__)

qrcode_url = "http://127.0.0.1:8000"

def cal_main():
    response = requests.get(qrcode_url)
    return response.json().get("fal")

@app.route("/generate", methods=["GET"])
def qrcode_func():
    result = cal_main()
    img = qrcode.make(result)
    img.save("some_file.png")
    filename = "some_file.png"
    print("qrcode returned")
    return send_file(filename, mimetype='image/png')
    
if __name__ == "__main__":
    app.run(port=5003)    