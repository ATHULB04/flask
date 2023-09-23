import pyrebase
import pdf
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
def done(name):
    localpath=""
    cloudpath=f"test/{name}.pdf"
    firebase.storage().child(cloudpath).download(localpath,filename="sample.pdf")
    return True
