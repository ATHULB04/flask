import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred) 
db=firestore.client()

def link(r,deadline,id,):
    idnum1=db.collection("idno").document("idno").get()
    idnum=int(idnum1.to_dict()['idno'])
    idnum+=1
    data={"id":id,"deadline":deadline,"work":r}
    db.collection("tasks").document(str(idnum)).set(data)
    db.collection("idno").document("idno").set({"idno":str(idnum)})
    return "done"
