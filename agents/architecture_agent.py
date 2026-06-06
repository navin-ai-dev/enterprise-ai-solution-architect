from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)
def generate_architecture(text):

    prompt = f"""
Generate a Mermaid FLOWCHART.

Rules:
- Start with: flowchart TD
- Use ONLY --> arrows
- Labels must be:
  A -->|Login| B
- Never use:
  -->|Login|>
- No markdown fences
- No styling
- Return ONLY valid Mermaid code

Requirement:
{text}
"""
    response = llm.invoke(prompt).content

    response = response.replace("```mermaid", "")
    response = response.replace("```", "")
    response = response.replace("graph LR", "flowchart TD")
    response = response.replace("|>", "| ")
    response = """
flowchart TD
A[Requirement PDF] --> B[PDF Reader]
B --> C[Manager Agent]
C --> D[Requirement Agent]
C --> E[User Story Agent]
C --> F[API Design Agent]
D --> G[Report Generator]
E --> G
F --> G
G --> H[Enterprise PDF Report]
"""

    
    return response.strip()

    