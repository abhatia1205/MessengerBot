import random

def get_author(db, name):
    authors = db.collection(u'authors')
    doc_ref = authors.document(name)
    return doc_ref
 
#chooses a random message to send to the user
def get_message(db, userId, text):
    for doc in db.collection(u'announcements').where(u'from', u'==', get_author(db, text)).stream():
        return doc.to_dict()['content']
    return "Message received"
