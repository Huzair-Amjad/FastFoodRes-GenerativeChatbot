import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv() #take environment variables from .env

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load your restaurant data
with open(r'D:\Users\Dell\FastFoodResChatbot\data.txt', 'r') as file:
    restaurant_data = file.read()

# Initialize the OpenAI LLM
llm = OpenAI(api_key=openai_api_key, temperature=0.3)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template=f"{restaurant_data}\nCustomer: {{question}}\nBot:",
)

# Create a LangChain LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit UI
st.title("Generative-Chatbot Through Langchain 🔗🦜")
st.title("Welcome To Huzi-Cafe 👋")
st.write("Feel free to ask about Huzi_Cafe 🤗")

question = st.text_input("Query:")
if question:
    response = chain.run(question=question)
    st.write(f"Bot: {response}")
