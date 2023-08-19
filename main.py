from flask import *
import response
app=Flask(__name__)


@app.route("/question",methods=['POST'])
def index():
    sentence=request.json['work']
    r=response.question(sentence)
    return {"result":r}

if __name__=="__main__":
    app.run(debug=True,port=6000)
