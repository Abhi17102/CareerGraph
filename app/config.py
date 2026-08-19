import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    COGNODB_URI: str = os.getenv("COGNODB_URI", "")
    COGNODB_USERNAME: str = os.getenv("COGNODB_USERNAME", "")
    COGNODB_PASSWORD: str = os.getenv("COGNODB_PASSWORD", "")

settings= Settings()