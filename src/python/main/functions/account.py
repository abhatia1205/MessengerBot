class account:
    localDb = None
    userRef = None
    googleUserRef = None

    def passAuthentication(self, email):
	""" Do something here"""

    def getDocRef(self, userId):
	for doc in localDb.collection('facebookUsers').where('userId', u'==', userId).stream():
	    return doc.reference
        return None

    def __init__(self, db, userId):
	self.localDb = db
        self.userRef = getDocRef(userId)
	if self.userRef == None:
	    userInfo = {'userId': userId, 'googleAccount': 'not_set'}
            self.userRef = self.localDb.collection('facebookUsers').create(userInfo)

    def connectToGoogleAccount(self, email):
        passAuthentication(email, userId)
        self.userRef.set({'googleAccount': email})

    def subscribe(self, author):
	userSnapshot = self.userRef.get().to_dict()
        if userSnapshot['account'] != 'not_set':
            
	 
        	
