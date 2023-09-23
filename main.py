from flask import *
app=Flask(__name__)
import firebase,pdf


@app.route("/question",methods=['POST'])
def index():
    name=request.json['name']
    print(name)
    r=firebase.done(str(name))
    if r==True:
        word=pdf.pdfread(name)
    return {"result":word}

if __name__=="__main__":
    app.run(debug=True,port=6000)
