from flask import *
import response,task
from flask_cors import CORS
app=Flask(__name__)
CORS(app)


@app.route("/question",methods=['POST'])
def index():
    sentence=request.json['work']
    deadline=request.json['deadline']
    id=request.json["id"]
    tech_needed=response.question(sentence)
    r=task.link(tech_needed,sentence,deadline,id)
    return {"result":r}

if __name__=="__main__":
    app.run(debug=True,port=6000)
