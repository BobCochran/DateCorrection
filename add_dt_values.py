#!/usr/bin/env python3
# script to test Zulhishman's MongoDB date and time issues.
from pymongo import MongoClient
import datetime
client = MongoClient()
db = client.zulhishman
collection = db.t1
post = {"author" : "Bob","text" : "first blog post","tags": ["mongodb", "python", "pymongo" ],"idt" : datetime.datetime.utcnow()}
collection.insert_one(post)
db.list_collection_names()
 
