# Mood-Based Motivational Quote Generator

from dotenv import load_dotenv
import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

print("================================================================================")
print("  Mood-Based Motivational Quote Generator  ")
print("================================================================================\n")

mood = input("How are you feeling today? : ")

messages = [
    ("system", "You are a mood-based motivational quote generator."),
    ("human", "My mood is {mood}.")
]

prompt_template = ChatPromptTemplate.from_messages(messages=messages)
prompt = prompt_template.invoke({"mood": mood})
response = model.invoke(prompt)

print("\nHere's your motivational quote:")
print("------------------------------------------------------------------------------------------------------")
print(response)
print("------------------------------------------------------------------------------------------------------\n")
print("Stay positive and keep going!")