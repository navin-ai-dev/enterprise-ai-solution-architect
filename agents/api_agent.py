from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

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