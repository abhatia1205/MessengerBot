import random

#chooses a random message to send to the user
def get_message(db, userId, text):
    announcements = db.collection(u'announcements')
    docs = announcements.where(u'title', u'==', u'Robotics First Meeting').stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    return "Message received"
