def single_agent(query):
    """
    Baseline Single-Agent Implementation
    """
    return f"Agent Response: {query}"


if __name__ == "__main__":
    while True:
        query = input("User Query: ")

        if query.lower() == "exit":
            break

        response = single_agent(query)
        print(response)