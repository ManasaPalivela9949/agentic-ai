def retrieve_context() -> str:
    print("[RETRIEVER] Reading knowledge.txt")
    with open("app/knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()
