import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import os

st.set_page_config(page_title="CSV Chatbot", layout="wide")
st.title("💬 Chat with your CSV")

# Upload CSV
csv_file = st.file_uploader("Upload your CSV file", type="csv")

# Enter OpenAI API Key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Ask a question
query = st.text_input("Ask a question about your CSV")

# Run when everything is provided
if csv_file and query and api_key:
    llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
    
    # Save uploaded CSV temporarily
    with open("uploaded.csv", "wb") as f:
        f.write(csv_file.getbuffer())

    agent = create_csv_agent(llm, "uploaded.csv", verbose=False)
    
    with st.spinner("Thinking..."):
        result = agent.run(query)
        st.success(result)
