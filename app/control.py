def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)

    if memory["completed"]:
        return "stop"

    # Step 1: Call LLM
    if len(memory["steps"]) == 0:
        print("[CONTROL] First step → CALL LLM")
        return "call_llm"

    # Step 2: Use tool
    if len(memory["steps"]) == 1:
        print("[CONTROL] Second step → USE TOOL")
        return "use_tool"

    # Handle tool failure
    last_step = memory["steps"][-1]
    if last_step == "TOOL_FAILED":
        if memory["tool_retries"] < 1:
            memory["tool_retries"] += 1
            print("[CONTROL] Tool failed → RETRY")
            return "use_tool"
        else:
            print("[CONTROL] Tool failed again → STOP")
            memory["completed"] = True
            return "stop"

    # Successful execution → stop
    print("[CONTROL] Tool succeeded → STOP")
    memory["completed"] = True
    return "stop"
