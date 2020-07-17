import json
from pymongo import MongoClient


def importMongo():

    client = MongoClient('localhost', 27017)
    db = client.dados
    collection_currency = db.socios

    print(collection_currency)

    with open('teste/socios_json/TEREZINHA FURTADO GUEDES.json') as f:
        file_data = json.load(f)

    # if pymongo >= 3.0 use insert_one() for inserting one document
    collection_currency.insert_one(file_data)
    client.close()


importMongo()
