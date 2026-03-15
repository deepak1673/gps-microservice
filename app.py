from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def location():
    gps_data = {
        "classroom": "IIIT Kottayam",
        "latitude": 9.5916,
        "longitude": 76.5222
    }
    return jsonify(gps_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)