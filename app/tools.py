import requests

def fetch_joke_tool() -> str:
    print("[TOOL] Calling external Joke API")

    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke",
        timeout=5
    )

    if response.status_code != 200:
        print("[TOOL] API failed")
        return "TOOL_FAILED"

    data = response.json()
    joke = f"{data['setup']} — {data['punchline']}"

    print("[TOOL] Joke fetched successfully")
    return joke