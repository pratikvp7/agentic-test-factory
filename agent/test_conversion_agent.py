import logging
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
FEATURES_DIR = BASE_DIR / "features"
INSTRUCTIONS = BASE_DIR / "instructions" / "test_writing_guide.md"
OUTPUT_DIR = BASE_DIR / "output"
MCP_SERVER = BASE_DIR / "mcp_server" / "server.py"
PYTHON = sys.executable
