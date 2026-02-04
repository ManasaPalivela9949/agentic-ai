def init_memory(goal: str) -> dict:
    print("[MEMORY] Initializing shared memory")
    return {
        "goal": goal,
        "plan": [],
        "current_step": 0,
        "results": [],
        "completed": False
    }
