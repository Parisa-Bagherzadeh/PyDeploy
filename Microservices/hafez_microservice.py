from flask import Flask, jsonify
import hafez



app = Flask(__name__)

@app.route("/fal", methods=["GET"])
def fal_hafez():
    omen = hafez.omen()
    fal = omen["interpretation"]
    return jsonify({"fal": fal})

if __name__ == "__main__":
    app.run(port=5001)
