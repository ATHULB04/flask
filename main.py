from flask import *
import pdfgen
app=Flask(__name__)

@app.route("/voice",methods=['POST'])
def index():
    user_question=request.json['sentence']
    r=pdfgen.voice(user_question)
    return({"result":r})

if __name__=="__main__":
    app.run(debug=True,port=6000)
