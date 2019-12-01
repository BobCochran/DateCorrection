#!/usr/bin/env python3
# script to test user's MongoDB date and time issues. Script adds one 
# document to a MongoDB database named "zulhisham" and a collection named
# "t1". This document uses the dateutil.parse utility to create a 
# valid ISO-8601 date object from a string value named timestamp. 
# The date object is stored in the variable dt2.
#
from pymongo import MongoClient
import datetime
from dateutil.parser import parse 
import pprint
timestamp = "2019-11-09T12:00:12.789Z"
dt2 = parse(timestamp)
client = MongoClient()
db = client.zulhishman
collection = db.t1
post = {"author" : "Bob","text" : "third blog post","tags": ["mongodb", "milliseconds", "parse" ],"idt" : dt2}
collection.insert_one(post)
pprint.pprint(db.list_collection_names())
 
