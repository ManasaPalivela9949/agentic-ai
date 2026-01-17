def init_memory(goal: str) -> dict:
    print("[MEMORY] Initializing memory")

    return {
        "goal": goal,
        "steps": [],
        "completed": False
    }