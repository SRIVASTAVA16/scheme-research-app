import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("\nSUCCESS: Your API key was loaded correctly!")
    print(f"Your key starts with: {api_key[:4]}\n")
else:
    print("\nFAILURE: The API key could not be found. Please check your .env file content.\n")