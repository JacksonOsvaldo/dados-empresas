#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the MongoClient class
import io
from pymongo import MongoClient

# import the Pandas library
import pandas

# these libraries are optional
import json
import time

# build a new client instance of MongoClient
mongo_client = MongoClient('localhost', 27017)

# create new database and collection instance
db = mongo_client.dados
col = db.empresas

# start time of script
start_time = time.time()

# make an API call to the MongoDB server
cursor = col.find()

# extract the list of documents from cursor obj
mongo_docs = list(cursor)

# restrict the number of docs to export
mongo_docs = mongo_docs[:50]  # slice the list
print("total docs:", len(mongo_docs))

# create an empty DataFrame for storing documents
docs = pandas.DataFrame(columns=[])

# iterate over the list of MongoDB dict documents
for num, doc in enumerate(mongo_docs):

    # convert ObjectId() to str
    doc["_id"] = str(doc["_id"])

# get document _id from dict
    doc_id = doc["_id"]

# create a Series obj from the MongoDB dict
series_obj = pandas.Series(doc, name=doc_id)

# append the MongoDB Series obj to the DataFrame obj
docs = docs.append(series_obj)

# only print every 10th document
if num % 10 == 0:
    print(type(doc))
    print(type(doc["_id"]))
    print(num, "--", doc, "\n")

"""
EXPORT THE MONGODB DOCUMENTS
TO DIFFERENT FILE FORMATS
"""
print("\nexporting Pandas objects to different file types.")
print("DataFrame len:", len(docs))

# export the MongoDB documents as a JSON file
docs.to_json("object_rocket.json")

# have Pandas return a JSON string of the documents
json_export = docs.to_json()  # return JSON data
print("\nJSON data:", json_export)

# export MongoDB documents to a CSV file
docs.to_csv("object_rocket.csv", ",")  # CSV delimited by commas

# export MongoDB documents to CSV
csv_export = docs.to_csv(sep=",")  # CSV delimited by commas
print("\nCSV data:", csv_export)

# create IO HTML string
html_str = io.StringIO()

# export as HTML
docs.to_html(
    buf=html_str,
    classes='table table-striped'
)

# print out the HTML table
print(html_str.getvalue())

# save the MongoDB documents as an HTML table
docs.to_html("object_rocket.html")

print("\n\ntime elapsed:", time.time()-start_time)
