from flask import Flask, request, jsonify
from flask_cors import cross_origin
from pymongo import MongoClient
from flask_cors import CORS
import datetime # included with python

# Get the path to the currently active Python interpreter to see if it's from the pyenv virtual environment's path
import sys # included with python
print(sys.executable) # Print's python interpreter path. Expect to be virtual environment's 

# Get the module import paths and it should have the pipenv virtual environment's path including the current app's path
# Print the paths where Python is importing modules from
for path in sys.path:
    print(path)

# For ObjectId to work
from bson import ObjectId # included with pymongo
import json # included with python

app = Flask(__name__)
CORS(app)

def is_running_in_docker():
    """Check if the current environment is a Docker container."""
    return os.path.exists('/.dockerenv')


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
# client = MongoClient(f"mongodb://host.docker.internal/")
# mongo_host = "host.docker.internal" if os.path.exists('/.dockerenv') else "localhost"
# client = MongoClient(f"mongodb://{mongo_host}:27017/")
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
    # Get the directory of the imported module
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

# Example request http://127.0.0.1:5001/files/read/foo.txt
@app.route("/files/read/<filename>", methods=["GET"])
def readFile2(filename):
    testInstructions = "This is to test whether the server can read a file from a folder that has been virtually mounted if running in Docker. If it can read, then it can write."
    if(filename):
        try:
            with open(f"./files/{filename}") as my_file:
                contents = my_file.read()
                return jsonify({"testInstructions": testInstructions, "filename":filename, "contents": contents}), 200
        except FileNotFoundError:
            return jsonify({"testInstructions": testInstructions, "error":"File not found"}), 200
        except IOError:
            return jsonify({"testInstructions": testInstructions, "error":"An error occurred while reading the file."}), 200
    else:
        return jsonify({"message": "No filename provided."}), 400

if __name__ == "__main__":
    # app.run(debug=True, port=5001)
    app.run(host='0.0.0.0', port=5001)
