from flask import *
import pdfgen
app=Flask(__name__)
from google.cloud import firestore
import firebase,time


db = firestore.Client.from_service_account_json("serviceAccount.json", project="studiesy")

# Replace "Notes" with the Firestore collection you want to listen to
# Replace "Physics" with the specific document ID you want to listen to, or None to listen to the entire collection
def call(subject): 
    collection_ref = db.collection("Notes").document(subject)

    # Store the latest transcribe data in a variable
    latest_transcribe_data = ""

    # Define a callback function to handle real-time updates
    def on_snapshot(doc_snapshot, changes, read_time):
        global latest_transcribe_data
        global subject1
        subject1=subject
        for doc in doc_snapshot:
            data = doc.to_dict()
            latest_transcribe_data = data.get('transcribe', '') 
            print(1)
            firebase.details(subject1,latest_transcribe_data) # Get the 'transcribe' value or an empty string if it doesn't exist
            time.sleep(200)
    # Listen to real-time updates
    doc_watch = collection_ref.on_snapshot(on_snapshot)

@app.route("/voice",methods=['POST'])
def index():
    user_question=request.json['sentence']
    r=pdfgen.voice(user_question)
    return({"result":r})

@app.route('/summary', methods=['GET'])
def get_latest_transcribe():
    subject=request.json['subject']
    call(subject)
    global latest_transcribe_data
    return jsonify({'latest_transcribe_data':"done"})

if __name__=="__main__":
    app.run(debug=True,port=6000)
