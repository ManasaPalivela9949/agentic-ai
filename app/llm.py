# import requests

# RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

# def call_llm(goal: str, context: str) -> str:
#     prompt = f"""
# Use the information below to answer clearly.

# CONTEXT:
# {context}

# TASK:
# {goal}
# """
#     response = requests.post(
#         RENDER_API_URL,
#         json={"prompt": prompt},
#         timeout=90
#     )
#     return response.json()["response"]

import requests

RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

def call_llm(prompt: str, context: str = "") -> str:
    try:
        response = requests.post(
            RENDER_API_URL,
            json={"prompt": prompt},
            timeout=90
        )
        response.raise_for_status()
        return response.json().get("response", "No response from LLM")

    except requests.exceptions.Timeout:
        return "[LLM ERROR] Timeout: LLM is sleeping or overloaded."

    except requests.exceptions.RequestException as e:
        return f"[LLM ERROR] {e}"
