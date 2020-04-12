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

def getDocumentReference(globalDb, authorName):
    authorRef = globalDb.collection(u'authors').document(authorName)
    for doc in globalDb.collection(u'announcements').where(u'from', u'==', authorRef).stream():
        print(doc)
    
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='1.0.0.0', port=7280)
