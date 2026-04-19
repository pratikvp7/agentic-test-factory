import sys
import logging
from pathlib import Path
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
from groq import Groq

# --- Setup ---
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
logger.info(f"ENV PATH: {env_path}")
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")  # ✅ Changed from OPENAI_API_KEY
logger.info(f"KEY FOUND: {bool(api_key)}")

if not api_key:
    raise ValueError(f"GROQ_API_KEY not found. Looked in: {env_path}")

mcp = FastMCP("test-factory")

client = Groq(api_key=api_key)  # ✅ Groq client, no base_url needed

@mcp.tool()
def generate_test_cases(feature_text: str) -> str:
    """Generate QA test cases for a given feature description."""
    logger.info(f"Generating test cases for: {feature_text}")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # ✅ Groq model
        messages=[
            {"role": "system", "content": "You are a senior QA engineer."},
            {"role": "user", "content": feature_text}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Smoke test
    result = generate_test_cases("Login with valid and invalid credentials")
    print(result, file=sys.stderr)
    mcp.run()