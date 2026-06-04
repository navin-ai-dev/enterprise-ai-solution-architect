from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def generate_risk_analysis(text):

    prompt = f"""
    Identify:

    Technical Risks
    Security Risks
    Performance Risks
    Business Risks

    Requirement:

    {text}
    """

    return llm.invoke(prompt).content