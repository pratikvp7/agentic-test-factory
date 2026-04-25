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

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/pratikvp7/agentic-test-factory.git
cd agentic-test-factory
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install groq mcp python-dotenv
```

**4. Add your API key**

Create a `.env` file in the root:

GROQ_API_KEY=your_key_here

Get a free key at [console.groq.com](https://console.groq.com)





---

## Run it

```bash
python agent/test_generator_agent.py login.md
```

To generate tests for a different feature:
```bash
python agent/test_generator_agent.py register.md
```

Generated test cases appear in `output/` and print to screen.




