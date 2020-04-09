import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request

def connectToTestDB():
    cred = credentials.Certificate('./lynbrook-high-school-test-credentials.json')
    firebase_admin.initialize_app(cred, {
         'databaseURL' : 'https://lynbrook-high-school.firebaseio.com'
    })

    db = firestore.client()
    
    print("Database connected")
    return db

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
