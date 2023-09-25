import psycopg2
import firebase_admin
from firebase_admin import credentials, db
import time
from datetime import datetime
import pandas as pd
import json
from pyrebase import pyrebase


# medium : https://parasmani300.medium.com/pyrebase-firebase-in-flask-d249a065e0df
# cred = credentials.Certificate('pg2fbtesting.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://pg2fbtesting-default-rtdb.asia-southeast1.firebasedatabase.app/'
# })
# print('working')

# ref = db.reference('/data')
# data = ref.get()
# length = len(data)

# print( ref.get()[length-1]['timestamp'])

from fastapi import FastAPI
import pyrebase
from pydantic import BaseModel
from typing import List



firebaseConfig = {
    'apiKey': "AIzaSyA-cd4vuWD7Hc7lMOMjtKy6fou6WUsCBmw",
    'authDomain': "pg2fbtesting.firebaseapp.com",
    'databaseURL': "https://pg2fbtesting-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "pg2fbtesting",
    'storageBucket': "pg2fbtesting.appspot.com",
    'messagingSenderId': "605577202780",
    'appId': "1:605577202780:web:09f6764767cfb4a1caea99",
    'measurementId': "G-H53T8T8K46"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# getting whole data
# data = db.child("data").get().val()

data = db.child("data").get()

# getting particular data
'''
for t in data.each():
    try:
        print(t.val()['detecteduv'])
    except TypeError:
        print('None')
'''

# shallow
## To return just the keys at a particular path use the shallow() method.

'''
all_keys = db.child('data').shallow().get()

print(all_keys.val())
'''


# update
## To update data for an existing entry use the update() method.

'''
db.child("data").child("1714").update({"timestamp": "2023-06-02 17:24:27.577360'"})
data = db.child("data").get().val()
print(data[1714])

'''

# order_by_child
## We begin any complex query with order_by_child().

'''
dataBy_timestamp = db.child("data").order_by_child("timestamp").get()
for d in dataBy_timestamp.val():
    print(d)
  '''  
    
# equal_to
## Return data with a specific value.
'''
datefilter = db.child("data").order_by_child("timestamp").equal_to('2023-09-18 15:15:01').get()
print(type(datefilter.val()))

'''
# start_at and end_at
## Specify a range in your data.
startDay = "2023-09-01 12:16:32.980251"
endday = "2023-09-01 12:16:36.996504"
datefilter = db.child("data").order_by_child("timestamp").start_at(startDay).end_at(endday).get()

print((datefilter.val()))







