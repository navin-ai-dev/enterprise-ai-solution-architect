from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_database_design(text):

    prompt = f"""
    Design database schema.

    Include:

    Tables
    Fields
    Relationships

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content