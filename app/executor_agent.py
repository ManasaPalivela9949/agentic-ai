from app.llm import call_llm
from app.retriever import retrieve_context

def executor_step(memory: dict, plan: str):
    print("\n[EXECUTOR] Executing plan:", plan)

    if plan == "call_llm":
        context = retrieve_context()
        answer = call_llm(memory["goal"], context)
        memory["results"].append(answer)
        print("\n[EXECUTOR] RESULT:\n", answer)
