from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import os

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "cats"})
print(prompt)