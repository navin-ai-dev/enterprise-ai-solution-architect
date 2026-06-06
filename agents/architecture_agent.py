from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)

def generate_architecture(text):

    prompt = f"""
    Based on this requirement,
    generate a Mermaid architecture diagram.

    Return ONLY Mermaid syntax.

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content