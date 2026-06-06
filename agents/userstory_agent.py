from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_user_stories(text):

    prompt = f"""
    You are a Business Analyst.

    Based on the requirement below, generate User Stories.

    Format:

    User Story 1:
    As a <user>,
    I want <feature>,
    So that <benefit>.

    User Story 2:
    As a <user>,
    I want <feature>,
    So that <benefit>.

    Requirement:
    {text}

    Generate 5-10 user stories.
    """

    response = llm.invoke(prompt)

    return response.content