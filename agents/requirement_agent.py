from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
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