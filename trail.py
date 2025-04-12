from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="aicinema69/CLAT_LLM",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    api_key = os.environ.get("HF_API_KEY")
)

print(llm.invoke("full form of clat"))