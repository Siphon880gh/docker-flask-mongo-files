from flask import Flask, request, jsonify
from flask_cors import cross_origin
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["docker-python-mongo"]


# http://127.0.0.1:5001/
@app.route("/", methods=["GET"])
def front():
    return jsonify({}), 200

# http://127.0.0.1:5001/db/seed
@app.route("/db/seed", methods=["GET"])
def dbSeed():
    return jsonify({}), 200

# http://127.0.0.1:5001/db/read
@app.route("/db/read", methods=["GET"])
def dbRead():
    return jsonify({}), 200


# http://127.0.0.1:5001/media/interim/property-details
@app.route("/files/read", methods=["POST"])
def readFile():
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
