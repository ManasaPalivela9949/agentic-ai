def init_memory(goal: str) -> dict:
    print("[MEMORY] Initializing shared memory")
    return {
        "goal": goal,
        "plan": [],        # REQUIRED for planner
        "results": [],     # Executor writes here
        "completed": False
    }
