import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model = "gemini-pro", google_api_key = api_key)

messages = [
  ("system", "You are a {subject} teacher."),
  ("human", "Explain me {topic} in just one sentence.")
]

print("*****************************************************************************\n                       Welcome to your one line AI teacher!!!\n*****************************************************************************")

subject = input("Please mention the subject: ")
topic = input("Which topic would you like to study: ")

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"subject": subject, "topic": topic})
response = model.invoke(prompt)

print("\nHere is your one line definition: ")
print(response, "\n")