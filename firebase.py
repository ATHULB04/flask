import os
import pdfgen
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred) 
db=firestore.client()

response_cache = {}
def promptmaker(transcribed_txt):
    instructions = """You are a chatbot who helps students learn. You make a summary based on the teacher's words.
    Only use words that the teacher told. Don't tell anything more or less than what the teacher told.
    Make sure the summary is not too long or too short.
    Make sure the summary is easy to understand.
    Make sure the summary only contains the contents told by the teacher.
    answer as a third person and remember you follow the format of a summary.
    """

    data = str(transcribed_txt)
    question = f"give me a summary of {transcribed_txt}"  # Corrected the variable name
    prompt = instructions + data + question
    return askgpt(prompt)

def askgpt(prompt):
    
    chat_model = ChatOpenAI(temperature=0.1, model='gpt-3.5-turbo', openai_api_key=os.environ.get("OPENAI_API_KEY"), max_tokens=250, stop=["\n"])
    
    if prompt in response_cache:
        return response_cache[prompt]

    output = chat_model([HumanMessage(content=prompt)])
    response = output.content
    response_cache[prompt] = response
    return response




def details(subject):
    list=db.collection("Notes").document(subject).get()
    if list.exists:  
        list=db.collection("Notes").document(subject).get()
        data=list.to_dict()
        sentence=data.get('transcribe', '').strip()
        print(sentence)
    else:
        print("does not exist")

    data=promptmaker(sentence)   #semd to gpt
    pdfgen.voice(sentence)
    print(3)
    db.collection("Notes").document(subject).update({"summary":data})
    return "done"








