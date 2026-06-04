from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

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