from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)

def generate_architecture(text):

    prompt = f"""
Generate a Mermaid FLOWCHART ONLY.

Rules:
1. Start with: flowchart TD
2. Use only nodes like A[User]
3. Use only arrows -->
4. Do NOT use participant
5. Do NOT use sequenceDiagram
6. Do NOT use style
7. Do NOT use markdown code fences
8. Return ONLY Mermaid code

Example:

flowchart TD
A[User] --> B[Login]
B --> C[API]
C --> D[(Database)]

Requirement:
{text}
"""
    response = llm.invoke(prompt).content

    response = response.replace("```mermaid", "")
    response = response.replace("```", "")
    response = response.replace("graph LR", "flowchart TD")

    return response.strip()

    