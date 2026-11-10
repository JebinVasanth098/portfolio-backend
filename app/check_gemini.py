# check_gemini.py
import importlib
import os
from pathlib import Path

try:
	importlib.import_module("dotenv").load_dotenv()
except ModuleNotFoundError as exc:
	if exc.name != "dotenv":
		raise
	env_file = Path(".env")
	if env_file.is_file():
		for line in env_file.read_text().splitlines():
			line = line.strip()
			if line and not line.startswith("#") and "=" in line:
				key, value = line.split("=", 1)
				os.environ.setdefault(key.strip(), value.strip().strip("\"'"))

from google import genai

client = genai.Client()
r = client.models.generate_content(model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"), contents="Say hello")
print(r.text)