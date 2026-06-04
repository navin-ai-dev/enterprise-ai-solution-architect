from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def generate_user_stories(text):

    prompt = f"""
    Generate agile user stories.

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content