# Simple Coding Agent

A minimal coding agent that uses a large language model (LLM) together with an E2B sandbox to generate and run code safely. This project is based on the deeplearning.ai course "Building Coding Agents with Tool Execution" and demonstrates how to combine tool schemas, a sandboxed executor, and an LLM-driven controller to perform small coding tasks.

## Features
- Generate and execute Python code inside an E2B Sandbox
- Read/write files within the sandbox
- Simple tool schemas for safe function calling
- Example agent that creates and stores outputs (CSV, TXT, PNG)

## Requirements
- Python >= 3.13
- An OpenAI API key
- An E2B API key
- Dependencies listed in pyproject.toml (e2b-code-interpreter, openai, python-dotenv)

## Setup
1. Create a virtual environment and install dependencies:
   - python -m venv .venv
   - source .venv/bin/activate
   - pip install -e .

2. Create a `.env` file at the project root with:
   - OPENAI_API_KEY=your_openai_key
   - E2B_API_KEY=your_e2b_key

3. Verify keys are loaded when running the example.

## Running the example
Run the main script:
- python main.py

The example prompts the agent to implement a small task (e.g., create a Caesar cipher, run it, and save results). The agent uses the E2B sandbox to execute code and writes/reads files through defined tools.

## Files of interest
- main.py — orchestrates the agent, prepares messages, and invokes tool calls.
- tools.py — lightweight tool wrappers for executing code and file IO inside the sandbox.
- schemas.py — JSON-like schemas describing available tools for the LLM.
- pyproject.toml — project metadata and dependencies.

## Security & Sandbox Notes
- Code execution occurs inside the E2B Sandbox (e2b-code-interpreter). The sandbox limits access and isolates execution from the host environment.
- Tools expose controlled operations (execute_code, read_file, write_file). Keep additional tooling minimal and validate inputs when adding new tools.
- Never expose sensitive host files via tool paths. Use sandboxed paths only.

## Extending the project
- Add more tool schemas to expand capabilities (e.g., data loaders, plotting utilities).
- Improve prompt engineering and system messages to guide safe behavior and reduce unwanted file access.
- Add tests around tool inputs/outputs and sandbox interactions.

## Credits
Based on the deeplearning.ai course "Building Coding Agents with Tool Execution".

## License
MIT License

Copyright (c) 2025 Pedro Ribeiro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.