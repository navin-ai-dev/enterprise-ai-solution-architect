from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_api_design(text):

    prompt = f"""
    Design REST APIs.

    Include:

    Endpoint
    Method
    Request
    Response

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content