import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred) 
db=firestore.client()


def prompt():
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.1)

    prompt = PromptTemplate(
        input_variables=["food"],
        template="write a detailed summary of {food} and explain it in a very understandable way.",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def question1(inputs):
    chain = prompt()
    return chain.run(inputs)


def details(subject):
    list=db.collection("Notes").document(subject).get()
    if list.exists:  
        list=db.collection("Notes").document(subject).get()
        data=list.to_dict()
        sentence=data.get('transcribe', '').strip()
        print(2)
    else:
        print("does not exist")

    data=question1(sentence)   #semd to gpt
    print(3)
    db.collection("Notes").document(subject).update({"summary":data})
    return "done"







