from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def generate_test_cases(text):

    prompt = f"""
    Generate detailed test cases.

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content