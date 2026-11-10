# app/config.py
import json
import os
from pathlib import Path

# app/config.py
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DEFAULT_ALLOWED_ORIGINS = ["https://portfolio-frontend-g371.onrender.com"]

class Settings:
    def __init__(self):
        # Required: the app refuses to start without these
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.gemini_model = os.getenv("GEMINI_MODEL")
        missing = [
            name for name, value in (
                ("GEMINI_API_KEY", self.gemini_api_key),
                ("GEMINI_MODEL", self.gemini_model),
            ) if not value
        ]
        if missing:
            raise ValueError(f"Missing required environment variable(s): {', '.join(missing)}")
        
        self.allowed_origins = list(DEFAULT_ALLOWED_ORIGINS)
        origins = os.getenv("ALLOWED_ORIGINS")
        if origins:
            try:
                configured_origins = json.loads(origins)
            except json.JSONDecodeError:
                configured_origins = [origin.strip() for origin in origins.split(",") if origin.strip()]
            self.allowed_origins.extend(
                origin for origin in configured_origins if origin not in self.allowed_origins
            )

        self.max_message_length = int(os.getenv("MAX_MESSAGE_LENGTH", "500"))
        self.max_history = int(os.getenv("MAX_HISTORY", "10"))


settings = Settings()
MODEL = settings.gemini_model
