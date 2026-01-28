import requests

RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

def call_llm(prompt: str, context: str) -> str:
    full_prompt = f"""
Use the following context to answer.

Context:
{context}

Question:
{prompt}
"""
    response = requests.post(
        RENDER_API_URL,
        json={"prompt": full_prompt}
    )
    return response.json()["response"]
