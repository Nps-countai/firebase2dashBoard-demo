import psycopg2
import firebase_admin
from firebase_admin import credentials, db
import time
from datetime import datetime,timedelta
import pandas as pd
import json


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

cred = credentials.Certificate('pg2fbtesting.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pg2fbtesting-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
print('working')
ref = db.reference('/data')
data = ref.get()
length = len(data)
print(length)

from datetime import datetime


current_datetime = datetime.now()
current_date = current_datetime.date()
print(current_date)
dayback = current_date - timedelta(days=1)

fcurrent_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S.%f")
fdayback = dayback.strftime("%Y-%m-%d %H:%M:%S.%f")

print('fdate:',fcurrent_datetime)
print('fdate:',fdayback)


startDay = "2023-09-01 12:16:32.980251"
endday = "2023-09-01 12:16:36.996504"
# query = ref.order_by_child('timestamp').start_at(startDay).end_at(endday).get()


# for value in query.values():
#     print(value)