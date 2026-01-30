def init_memory(goal: str) -> dict:
    print("[MEMORY] Initializing fresh memory")
    return {
        "goal": goal,
        "steps": [],
        "completed": False
    }
