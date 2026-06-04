from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

response = llm.invoke(
    "Tell me about Artificial Intelligence"
)

print(response.content)