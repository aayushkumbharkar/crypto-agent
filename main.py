from core.orchestrator import run_agent

if __name__ == "__main__":
    query = input("Enter coin (default: bitcoin): ") or "bitcoin"

    result = run_agent()

    print("\n=== AI Decision ===")
    print(result["decision"])

    print("\n=== Critic Review ===")
    print(result["critique"])
