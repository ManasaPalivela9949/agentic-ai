def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)

    if memory["completed"]:
        return "stop"

    # Step 1: Ask LLM
    if len(memory["steps"]) == 0:
        print("[CONTROL] First step → CALL LLM")
        return "call_llm"

    # Step 2: Use external tool
    if len(memory["steps"]) == 1:
        print("[CONTROL] Second step → USE TOOL")
        return "use_tool"

    # Step 3: Stop
    print("[CONTROL] All steps done → STOP")
    memory["completed"] = True
    return "stop"
