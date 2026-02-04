from app.control import decide_next_step
from app.memory import init_memory
from app.llm import call_llm
from app.tools import observe_output
from app.retriever import retrieve_context

def run_agent(goal: str):
    memory = init_memory(goal)

    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)

    while True:
        step = decide_next_step(memory)

        if step == "call_llm":
            context = retrieve_context()
            answer = call_llm(goal, context)
            memory["steps"].append(answer)
            print("\n[AGENT] FINAL ANSWER:\n", answer)

        elif step == "observe":
            observe_output(memory["steps"][-1], memory)

        elif step == "stop":
            print("\n[AGENT] Agent stopped cleanly")
            break
