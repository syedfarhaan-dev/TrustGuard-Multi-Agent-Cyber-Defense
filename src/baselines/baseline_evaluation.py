from single_agent import single_agent

test_queries = [
    "What is prompt injection?",
    "Explain agent security.",
    "What is memory poisoning?"
]

for query in test_queries:
    response = single_agent(query)

    print("\nQuery:", query)
    print("Response:", response)