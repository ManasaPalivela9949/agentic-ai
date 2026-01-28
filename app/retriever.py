def retrieve_context(query: str) -> str:
    print("[RETRIEVER] Searching knowledge base")

    try:
        with open("knowledge.txt", "r") as f:
            lines = f.readlines()

        matched = []
        for line in lines:
            if any(word.lower() in line.lower() for word in query.split()):
                matched.append(line.strip())

        if not matched:
            return "No relevant context found."

        return " ".join(matched)

    except FileNotFoundError:
        return "Knowledge file not found."