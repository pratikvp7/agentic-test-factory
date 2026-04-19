import sys
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# Setup
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR        = Path(__file__).resolve().parent.parent
FEATURES_DIR    = BASE_DIR / "features"
INSTRUCTIONS    = BASE_DIR / "instructions" / "test_writing_guide.md"
OUTPUT_DIR      = BASE_DIR / "output"
MCP_SERVER      = BASE_DIR / "mcp_server" / "server.py"
PYTHON          = sys.executable

load_dotenv(BASE_DIR / ".env")
OUTPUT_DIR.mkdir(exist_ok=True)


# Step 1: Ready input files
def read_files(feature_file: str) -> tuple[str, str]:
    feature_path = FEATURES_DIR / feature_file

    if not feature_path.exists():
        raise FileNotFoundError(f"Feature file not found: {feature_path}")
    if not INSTRUCTIONS.exists():
        raise FileNotFoundError(f"Instructions file not found: {INSTRUCTIONS}")

    feature_text      = feature_path.read_text()
    instructions_text = INSTRUCTIONS.read_text()

    logger.info(f"Feature file loaded:      {feature_path}")
    logger.info(f"Instructions file loaded: {INSTRUCTIONS}")

    return feature_text, instructions_text


# Step 2: Build a prompt
def build_prompt(feature_text: str, instructions_text: str) -> str:
    prompt = f"""
You are a senior QA engineer working on a banking web application called ParaBank.

=== INSTRUCTIONS — HOW TO WRITE TEST CASES ===
{instructions_text}

=== FEATURE UNDER TEST ===
{feature_text}

=== YOUR TASK ===
Using the instructions and rules above, generate complete test cases for this feature.

Follow these rules strictly:
- Use the correct ID prefix as defined in the instructions (e.g. LGN- for Login)
- Every verification step MUST start with "Verify that"
- Every action step MUST start with the correct verb: Navigate, Click, Enter, Select, Type, Scroll, Clear, Upload, Hover over, Submit
- Cover all of these: happy path, negative cases, empty fields, boundary values, edge cases, security basics (SQL injection, XSS)
- Do NOT invent fields, flows or error messages not described in the feature file
- Precondition must describe the exact state before the test — never write "None"
- Each test case must be fully independent — no test should depend on another
"""
    return prompt.strip()


# Step 3: Call MCP tool
async def call_mcp_tool(prompt: str) -> str:
    server_params = StdioServerParameters(
        command=PYTHON,
        args=[str(MCP_SERVER)]
    )

    logger.info("Starting MCP server...")
    logger.info("Calling generate_test_cases tool...")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "generate_test_cases",
                arguments={"feature_text": prompt}
            )

            return result.content[0].text


# Step 4: Save output
def save_output(feature_file: str, test_cases: str) -> Path:
    feature_name = Path(feature_file).stem          # login.md → login
    output_file  = OUTPUT_DIR / f"{feature_name}_tests.txt"
    output_file.write_text(test_cases)
    logger.info(f"Test cases saved to: {output_file}")
    return output_file


# Orchestrates all steps
async def run(feature_file: str):
    # Step 1 — Read files
    feature_text, instructions_text = read_files(feature_file)

    # Step 2 — Build prompt
    prompt = build_prompt(feature_text, instructions_text)

    # Step 3 — Call MCP tool → Groq generates test cases
    test_cases = await call_mcp_tool(prompt)

    # Step 4 — Save to output/
    output_file = save_output(feature_file, test_cases)

    # Print to screen
    print("\n" + "=" * 60)
    print(f"  GENERATED TEST CASES — {feature_file}")
    print("=" * 60)
    print(test_cases)
    print("=" * 60)
    print(f"\nSaved to: {output_file}")


if __name__ == "__main__":
    # Usage:
    #   python agent/test_generator_agent.py login.md
    #   python agent/test_generator_agent.py register.md
    feature = sys.argv[1] if len(sys.argv) > 1 else "login.md"
    asyncio.run(run(feature))