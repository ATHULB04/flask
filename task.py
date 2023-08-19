import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred) 
db=firestore.client()

def link(link,deadline):
    id=1013
    data={"id":link,"deadline":deadline}
    db.collection("tasks").document(str(id)).set(data)
    id+=1
    return "done"

link("https://github.com/RivaanRanawat/flutter-amazon-clone-tutorial",1101)