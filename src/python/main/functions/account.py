import utils as ut

class account:
    localDb = None
    userRef = None
    googleUserRef = None

    def passAuthentication(self, email):
	""" Do something here"""

    def __init__(self, db, userId):
	self.localDb = db
        self.userRef = ut.get_ref(db, 'announcements', 'userId', userId)
	if self.userRef == None:
	    userInfo = {'userId': userId, 'googleAccount': 'not_set', 'subscribed': []}
            self.userRef = ut.createDoc(db, col, userInfo)
 
    def connectToGoogleAccount(self, email):
        passAuthentication(email, userId)
        self.userRef.set({'googleAccount': email})

    def getAuthorRef(self, author):
        for doc in localDb.collection('authors').where('author', u'==', author).stream():
            return doc.reference
        return None

    def subscribe(self, author):
        authorRef = getAuthorRef(author)
        currentList = userRef.get().to_dict()['subscribed']
        authoRef.set({'subscribed': currentList + List(authorRef)}, merge=True)
