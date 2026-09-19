import os
from dotenv import load_dotenv

load_dotenv()

# استدعاء مفتاح Tavily من حساب التطوير أو البرودكشن

TAVILY_API_KEY = os.getenv("API")