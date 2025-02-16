# Product review generator

import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model = "gemini-pro", google_api_key = api_key)

messages = [
  ("system", "This is the product: {product}."),
  ("human", "Give me a {rating}-star rating for this product.")
]

print("*****************************************************\n                    Welcome to an AI powered Product Review Generator\n*****************************************************")

product = input("Enter the product: ")
rating = input("Enter the rating for the review between (1-5): ")

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"product": product, "rating": rating})
response = model.invoke(prompt)

print("\nHere is your review: ")
print(response, "\n")