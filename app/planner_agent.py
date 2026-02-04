def planner_step(memory: dict) -> str:
    print("\n[PLANNER] Reviewing memory:", memory)

    if not memory["plan"]:
        step = "call_llm"
        memory["plan"].append(step)
        print("[PLANNER] Plan created:", step)
        return step

    memory["completed"] = True
    print("[PLANNER] Plan complete → STOP")
    return "stop"
