from flask import *
import os
app=Flask(__name__)

import pyrebase

config ={
 "apiKey": "AIzaSyAvXSSHSTbm7vXR_0mySUwOPJWlvZ1E480",
  "authDomain": "studiesy.firebaseapp.com",
  "databaseURL": "https://studiesy-default-rtdb.firebaseio.com",
  "projectId": "studiesy",
  "storageBucket": "studiesy.appspot.com",
  "messagingSenderId": "1070198266308",
  "appId": "1:1070198266308:web:ee0546f9c31da90d256c91",
  "measurementId": "G-SPW2YS1XML"
}
firebase = pyrebase.initialize_app(config)



@app.route("/",methods=['POST'])
def index():
    name=request.json['name']
    localpath=f"{name}.pdf"
    cloudpath=f"test/{name}.pdf"
    firebase.storage().child(cloudpath).download(filename="test.pdf")
    return {"result":"done"}

if __name__=="__main__":
    app.run(debug=True,port=6000)
