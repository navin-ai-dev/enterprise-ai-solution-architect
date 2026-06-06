from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def analyze_requirements(text):

    prompt = f"""
    Analyze this requirement.

    Return:

    1. Project Objective
    2. Key Features
    3. Stakeholders
    4. Functional Requirements

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content