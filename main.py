from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model='minimax-m2.7:cloud')
template = """
you are a helpful assistant. Answer the question below in short and precise.
here are some relevent reviews: {reviews}
Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
while True:
    question = input("Ask a question: write exit to quit: ")
    print("\n\n ")
    if question == 'exit':
        print("Exiting..."  )
        break
    
    result =chain.invoke({"reviews": [], "question": question})
   
    