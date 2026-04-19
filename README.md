# Agentic Test Factory

An AI agent that reads feature descriptions and automatically generates 
structured test cases using an LLM (Groq + Llama 3.3 70B) via an MCP server.

Built as a learning project to explore agentic AI workflows in QA automation.
Test application used: [ParaBank](https://parabank.parasoft.com/parabank/index.htm)

---

## How it works

1. You describe a feature in plain English inside `features/`
2. The agent reads that + the test writing rules from `instructions/`
3. It calls an MCP tool which sends a smart prompt to Groq
4. Groq generates structured test cases
5. Output is saved to `output/`

