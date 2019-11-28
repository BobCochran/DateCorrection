#!/usr/bin/env python3
# script to test Zulhishman's MongoDB date and time issues.
from pymongo import MongoClient
import datetime
from dateutil.parser import parse 
import pprint
timestamp = "2019-11-09T12:00:12.000Z"
dt2 = parse(timestamp)
client = MongoClient()
db = client.zulhishman
collection = db.t1
post = {"author" : "Bob","text" : "second blog post","tags": ["mongodb", "python", "parse" ],"idt" : dt2}
collection.insert_one(post)
pprint.pprint(db.list_collection_names())
 
