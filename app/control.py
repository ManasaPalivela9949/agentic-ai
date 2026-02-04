def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Memory state:", memory)

    if memory["completed"]:
        return "stop"

    if len(memory["steps"]) == 0:
        return "call_llm"        # REASON → ACT (LLM)

    if len(memory["steps"]) == 1:
        return "observe"         # REASON → OBSERVE

    memory["completed"] = True
    return "stop"
