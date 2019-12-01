#!/usr/bin/env python3
# script to test user's MongoDB date and time issues. Script adds one 
# document to a MongoDB database named "fixdates" and a collection named
# "t1". This script uses the python datetime.datetime.utcnow() method to add a
# valid ISO-8601 date object as the value of the key idt.
#
from pymongo import MongoClient
import datetime
client = MongoClient()
db = client.fixdates
collection = db.t1
post = {"author" : "Bob","text" : "first blog post","tags": ["mongodb", "python", "pymongo" ],"idt" : datetime.datetime.utcnow()}
collection.insert_one(post)
db.list_collection_names()
 
