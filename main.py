import openai
import langchain
import os
from langchain.llms.openai import OpenAI

llm = OpenAI(temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))

print(llm.predict("What is the capital of India?"))
