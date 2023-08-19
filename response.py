import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')

def prompt():
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.1)

    prompt = PromptTemplate(
        input_variables=["work"],
        template="what tech stacks are present in the work statement {work}.return only name of tech stacks like this 'django,python,react'",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def question(inputs):
    chain = prompt()
    response = chain.run(inputs)
    
    
    tech_stacks = [stack.strip() for stack in response.split(',') if stack.strip()]
    
    return tech_stacks


