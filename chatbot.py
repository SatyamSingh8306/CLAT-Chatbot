from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import MessagesPlaceholder
from faiss_database import embeddingModel
import os

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
DB_FAISS_PATH = "vectorstores/db_faiss"
db = FAISS.load_local(DB_FAISS_PATH, embeddingModel,allow_dangerous_deserialization=True)

context = db.as_retriever(top_k=5)

def chatbot(input,context,chat_history=[]):
    prompt = ChatPromptTemplate([
        ("system", "You are an expert in CLAT 2025. Your job is to answer questions accurately and provide detailed explanations."),
        ("ai", "Answer the question precisely and give the explanation if you need the context then use this context: {context}"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="chat_history")
    ])

    # llm = HuggingFaceEndpoint(
    #     repo_id="aicinema69/CLAT_LLM",
    #     task="text-generation",
    #     max_new_tokens=512,
    #     do_sample=False,
    #     repetition_penalty=1.03,
    #     api_key = os.environ.get("HF_API_KEY")
    # )


    # model = ChatHuggingFace(llm=lm)

    model = ChatGroq(
        model = "llama3-8b-8192",
        temperature = 0.5,
        api_key = GROQ_API_KEY,
        max_tokens=3000

    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    return chain.invoke({"input": input,"context": context,"chat_history": chat_history})

if __name__ == "__main__":
    print(chatbot("How many questions are there in the English section",context))





