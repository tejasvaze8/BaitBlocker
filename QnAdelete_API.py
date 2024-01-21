import requests
import os
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS


os.environ["OPENAI_API_KEY"] = "insert API key"
MONGO_URI = "mongodb+srv://tvaze:gmjg94r0F7Y8fMWW@cluster0.koafm.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
CORS(app, resources={"/delete_all": {"origins": "*"}})  # Allow any origin


# MongoDB setup (assuming MONGO_URI and other constants are defined)
client = MongoClient(MONGO_URI)
DB_NAME = "BaitBlocker"
COLLECTION_NAME = "QandAvectorStore"
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

@app.route('/delete_all', methods=['POST'])
def delete_all():
    print("Deleting all documents")
    MONGODB_COLLECTION.delete_many({})
    payload = {'status': 'success'}
    return payload # Indicates success but no content to return



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
