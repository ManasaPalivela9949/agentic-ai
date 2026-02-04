def observe_output(text: str, memory: dict):
    print("\n[OBSERVE] Reviewing output:")
    print(text)

    # 🔑 CRITICAL: update memory after observation
    memory["steps"].append("observed")
