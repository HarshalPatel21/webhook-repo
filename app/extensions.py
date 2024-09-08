from flask_pymongo import PyMongo
from .Helper.dbSchema import schema
from pymongo.errors import CollectionInvalid
from .Helper.jsonData import jsonDataParser 
from datetime import datetime

db = None

def setUpDatabase(app):
    global db
    app.config["MONGO_URI"] = "mongodb://localhost:27017/webhookDB"
    mongo = PyMongo(app=app)

    db = mongo.db
    create_collection_with_schema("webhooks")

    return app

def getDb():
    return db

def create_collection_with_schema(collection_name):
    try:
        if collection_name not in db.list_collection_names():
            dbSchema = schema
            db.create_collection(collection_name, validator=dbSchema)
        else: 
            print(f"Collection '{collection_name}' already exists.")
    
    except CollectionInvalid as e:
        print(f"Error creating collection: {e}")

def insert_data(data,webhook_event):
    
    try:
        document = jsonDataParser(data=data ,webhook_event = webhook_event)
        document['timestamp'] = str(datetime.now())
        db.webhooks.insert_one(document)

        print("insertion success")
        return "Success"

    except Exception as e :
        print(e)
        return "Fail"