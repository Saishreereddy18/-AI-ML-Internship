
import logging
import os
from dotenv import load_dotenv

load_dotenv()

os.makedirs("logs", exist_ok=True)

log_level = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(os.getenv("APP_NAME", "AI_Career_Copilot"))
