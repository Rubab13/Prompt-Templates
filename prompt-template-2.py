from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import os

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

messages = [
  ("system", "You are a comedian whoe tells jokes about {topic}."),
  ("human", "Tell me {count} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "cats", "count": 2})
print(prompt)

response = model.invoke(prompt)
print(response)

# Whenever you want to do string interpolation, use tuples.