#path src/database.py
from pymongo import MongoClient #import pymongo
import logging  # import logging

#defining configuration of logging
logging.basicConfig(filename="C:/Users/paulb/Documents/Coding/Python latest Projects/Exchange/log/log.txt", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


validator_class={'$jsonSchema': {
                'bsonType': 'object',
                'additionalProperties': True,
                'required': ["date","temp", "hum"],
                "properties": {
                    "date":{
                        "bsonType": "string",
                        "description": "date"
                    },
                    "temp":{
                        "bsonType": "int",
                        "description": "temp"
                    },
                    "hum":{
                        "bsonType": "int",
                        "description": "hum"
                    }
                }
            }}

client = MongoClient("mongodb://localhost:27017")

#creates database if not there
exchange = client.echange

#defins database and collection in variable db
db = MongoClient("mongodb://localhost:27017/")['exchange']

def create_collection(coltype,validator):
    try:
        db.create_collection(coltype, validator=validator)
        logging.error("Collection created")
        return True
    except Exception as e:
        logging.error(e)
        return False

def create_doc(doctype,insertdata):
    db[doctype].insert_one(insertdata)
    logging.error("Document created")
    return True

def read_onedoc(coltype,finddata):
    logging.error("Document read")
    return db[coltype].find(finddata)

def read_multipledocs(coltype,finddata):
    logging.error("Documents read")
    alldatalist = []
    for x in db[coltype].find({},finddata):
        alldatalist.append(x)
    return alldatalist



