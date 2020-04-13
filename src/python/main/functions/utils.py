def get_ref(db, col, identifier, obj):
    for doc in db.collection(col).where(identifier, u'==', obj).stream():
        return doc.reference
    return None

def get_field(ref, field):
    return ref.get().to_dict()[field]

def update(ref, key, val):
    ref.set({key: val}, merge=True)

def addEntry(ref, key, val):
    currList = get_field(ref, key)
    ref.set({key: currList + [val]}, merge=True)

def createDoc(db, col, data, docId=None):
    db.collection(col).add(data, docId)

def getSingle(ref, key, obj):
    currMap = get_field(ref, key)
    return currMap[obj] 
    
def updateSingle(ref, key, subkey, obj):
    currMap = get_field(ref, key)
    currMap[subkey] = obj
    update(ref, key, currentMap)
