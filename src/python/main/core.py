def get_author(db, name):
    authors = db.collection(u'authors')
    doc_ref = authors.document(name)
    return doc_ref
 
def get_message(db, userId, text):
    for doc in db.collection(u'announcements').where(u'from', u'==', get_author(db, text)).stream(): 
        return doc.to_dict()['content']
    return "Message received"

def get_reference(db, text):
    for doc in db.collection(u'announcements').where(u'from', u'==', get_author(db, text)).stream():
        return doc.reference
    return None

def message(db, text):
    return get_message(db, "random", text)
