# from app.llm import call_llm
# from app.retriever import retrieve_context

# def executor_step(memory: dict, plan: str):
#     print("\n[EXECUTOR] Executing plan:", plan)

#     if plan == "call_llm":
#         context = retrieve_context()
#         answer = call_llm(memory["goal"], context)
#         memory["results"].append(answer)
#         print("\n[EXECUTOR] RESULT:\n", answer)



from app.llm import call_llm
from app.retriever import retrieve_context

def executor_step(memory: dict, plan: str):
    print("\n[EXECUTOR] Executing plan:", plan)

    if plan == "call_llm":
        context = retrieve_context()
        answer = call_llm(memory["goal"], context)
        memory["results"].append(answer)

    elif plan == "review_result":
        print("\n[REVIEW RESULT]")
        if memory["results"]:
            print(memory["results"][-1])
            print("\n[REVIEW] Result reviewed successfully ✅")
        else:
            print("[REVIEW] No result found to review")

    else:
        print("[EXECUTOR] Unknown plan step")
