from flask import Flask, request, jsonify
from flask_cors import cross_origin
from pymongo import MongoClient
from flask_cors import CORS
import datetime

# For ObjectId to work
from bson import ObjectId
import json

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["docker-python-mongo"]


# Custom JSONEncoder to serialize ObjectId
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

# http://127.0.0.1:5001/
@app.route("/", methods=["GET"])
def front():
    return jsonify({"message": "This is to test a Dockerized Flask + MongoDB server that's been Gunicorned, and whether it can still have access to a folder that has been virtually mounted. Just to easily test all routes, I have them as GET."}), 200

# http://127.0.0.1:5001/db/seed
@app.route("/db/seed", methods=["GET"])
def dbSeed():
    foo_collection = db['foo']
    foo_collection.delete_many({})
    timeVal = str(datetime.datetime.now(datetime.timezone.utc))
    inserted = foo_collection.insert_one({"time":timeVal})
    _id = str(inserted.inserted_id)
    
    print("Data seeded successfully.")
    
    return jsonify({"seeded":{"_id":_id, "time":timeVal}}), 201

# http://127.0.0.1:5001/db/create
@app.route("/db/create", methods=["GET"])
def dbCreate():
    foo_collection = db['foo']
    # foo_collection.delete_many({})
    timeVal = str(datetime.datetime.now(datetime.timezone.utc))
    inserted = foo_collection.insert_one({"time":timeVal})
    _id = str(inserted.inserted_id)
    
    print("Data seeded successfully.")
    
    return jsonify({"seeded":{"_id":_id, "time":timeVal}}), 201


# http://127.0.0.1:5001/db/read
@app.route("/db/read", methods=["GET"])
def dbRead():
    # Retrieve all documents
    foo_collection = db['foo']
    documents = list(foo_collection.find())
    
    # Serialize the list of documents using the custom JSONEncoder
    json_data = json.dumps(documents, cls=JSONEncoder)

    return json_data, 200


# http://127.0.0.1:5001/files/read
@app.route("/files/read", methods=["POST"])
def readFile():
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
