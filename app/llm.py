import requests

RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

def call_llm(goal: str, context: str) -> str:
    prompt = f"""
Use the information below to answer clearly.

CONTEXT:
{context}

TASK:
{goal}
"""
    response = requests.post(
        RENDER_API_URL,
        json={"prompt": prompt},
        timeout=20
    )
    return response.json()["response"]
