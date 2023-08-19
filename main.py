from flask import *
import response,task
app=Flask(__name__)


@app.route("/question",methods=['POST'])
def index():
    sentence=request.json['work']
    r=response.question(sentence)
    return {"result":r}
@app.route("/task1",methods=['POST'])
def index1():
    task1=request.json['task']
    deadline=request.json['deadline']
    r =task.link(task1,deadline)
    return r

if __name__=="__main__":
    app.run(debug=True,port=6000)
