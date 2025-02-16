# Fictional Story generator Generator

from dotenv import load_dotenv
import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

print("================================================================================")
print("  Fictional Story generator Generator  ")
print("================================================================================\n")

genre = input("Enter the genre: ")
main_character = input("Enter the Main Character: ")
setting = input("Enter the setting: ")

messages = [
    ("system", "You are a short fictional story generator."),
    ("human", "Write a {genre} short story about {main_character} in a {setting}.")
]

prompt_template = ChatPromptTemplate.from_messages(messages=messages)
prompt = prompt_template.invoke({"genre": genre, "main_character":main_character, "setting":setting})
response = model.invoke(prompt)

# Display response
print("\nHere's your short sci-fi story:")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(response)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print("Hope you liked it!")