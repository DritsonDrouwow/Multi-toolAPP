import os 
from dotenv import load_dotennv

load_dotennv()

HF_API_KEY = os.getenv("HF_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
