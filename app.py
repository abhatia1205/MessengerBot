import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from firebase_admin import db
#from google.cloud import firestore
import random
from flask import Flask, request
from pymessenger.bot import Bot
from src.python.main.core import get_message

def connectToDB():
    cred = credentials.Certificate('./lynbrook-high-school-credentials.json')
    firebase_admin.initialize_app(cred, {
         'databaseURL' : 'https://lynbrook-high-school.firebaseio.com'
    })

    db = firestore.client()
    return db

app = Flask(__name__)
ACCESS_TOKEN = 'EAAIY9ZCGG5P8BANNpChCn9QEnZCqgmZCod9Ru6aVl3eHsyFLLMoq7tSa7ZBAGEafuNy6ddnYt4QY15aMFhztzxPtro4vPeWWGHgxhM4SzBtMn7YBPqV2ski842KQlHLT2hkM4DB4AScUBBc5TyEqVqIlUEzpWy0WqWxmZAoTkpNov3ly9qLYZC'
VERIFY_TOKEN = 'SMART_ML_BOT'
bot = Bot(ACCESS_TOKEN)
dbRef = connectToDB()

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message(): 
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message(dbRef, message['sender']['id'], message['message'].get('text'))
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()


