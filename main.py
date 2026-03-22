from core.orchestrator import run_agent

if __name__ == "__main__":
    query = input("Enter coin (default: bitcoin): ") or "bitcoin"

    result = run_agent()

    print("\n=== AI Decision ===")
    print(f"Decision: {result['decision']}")
    print(f"Reason: {result['reason']}")
    print(f"Confidence: {result['confidence']}%")
