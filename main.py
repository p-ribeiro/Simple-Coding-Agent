import os
from re import M
from dotenv import load_dotenv
from openai import OpenAI
from e2b_code_interpreter import Execution, Sandbox

import sys
from io import StringIO
from typing import Callable, Literal, Optional
import json

from tools import execute_tool, tools
from schemas import tools_schemas

load_dotenv()

# check if API keys are set
if not os.getenv("OPENAI_API_KEY"):
    print("⚠️ OPENAI_API_KEY not found!")
    print("Please create a .env with your OpenAI API key.")
    exit(1)
elif not os.getenv("E2B_API_KEY"):
    print("⚠️ E2B_API_KEY not found!")
    print("Please add your E2B API key to the .env file.")
    exit(1)
else:
    print("✅ API Keys loaded successfully")
    

def coding_agent(
    client: OpenAI,
    query: str,
    tools: dict[str, Callable],
    tools_schemas: list[dict],
    sbx: Sandbox,
    system: Optional[str] = "You are a senior Python programmer." ,
    model: Literal["gpt-4.1-mini", "gpt-5-mini"] = "gpt-5-mini",
    messages: Optional[list[dict]] = None,
    max_steps: int = 5,
    **model_kwargs,
):
    if messages is None:
        messages = []
    
    messages.append({"role": "user", "content": query})
    messages.append({"role": "developer", "content": system})
    steps = 0
    
    while steps < max_steps:
        response = client.responses.create(
            model = model,              #type: ignore
            input = [*messages],        #type: ignore
            tools=tools_schemas,        #type: ignore
            **model_kwargs,
        )
        
        print(f"[#{steps}-step]")
        has_function_call = False
        
        for part in response.output:
            messages.append(part)
            if part.type == "message":
                print(f"[agent] {response.output_text}")
            elif part.type == "function_call":
                has_function_call = True
                name = part.name
                print(f"[agent][{name}] executing...")
                result = execute_tool(name, part.arguments, tools, sbx=sbx)
                print(f"[{name}] {result}")
                messages.append(
                    {
                        "type": "function_call_output",
                        "call_id": part.call_id,
                        "output": json.dumps(result)
                    }
                )
        if not has_function_call:
            print("[agent] all tasks completed")
            break
        steps += 1
        

def main():
    
    client = OpenAI()
    sbx = Sandbox.create(timeout = 60*60)
    
    query = """Your task is:
    1. Write me a caesar cipher function
    2. Encode the following message: "This is a secret"
    3. Use a random cipher shift
    4. Run the function with the cipher shift you chose and the message I provided
    5. Print back the ciphered message, and the cipher shift chosen.
    6. Save it to secret.txt file in the current folder.
    7. Return the contents of secrets.txt.
    """
    
    coding_agent(client, query, tools, tools_schemas, sbx)
    
if __name__ == "__main__":
    main()