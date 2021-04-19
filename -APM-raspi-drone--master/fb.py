import os     #importing os library 
import time   #importing time 
from firebase import firebase 
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyB8PXmbAhCglMcvTQYYEkEg_H0KlUQHgl4",
    "authDomain": "seabin-be632.firebaseapp.com",
    "databaseURL": "https://seabin-be632.firebaseio.com",
    "projectId": "seabin-be632",
    "storageBucket": "seabin-be632.appspot.com",
    "messagingSenderId": "406649588495",
    "appId": "1:406649588495:web:f90ba06ea477d256820c7a",
    "measurementId": "G-VXF85SSYEC"
};

firebaseConn = pyrebase.initialize_app(firebaseConfig)

connection = firebase.FirebaseApplication('https://seabin-be632.firebaseio.com',None)

db = firebaseConn.database()

while True:
    inp = db.child("seabin").child("motion").get()
    print(inp.val())
    f = open("motion.txt", "w")
    f.write(inp.val())
