from dotenv import load_dotenv
import os

load_dotenv()

def simple_agent(user_prompt):
    """
    Baseline Single-Agent System
    """
    return f"Agent Response: {user_prompt}"

if __name__ == "__main__":
    while True:
        prompt = input("\nUser: ")

        if prompt.lower() == "exit":
            break

        response = simple_agent(prompt)
        print(response)