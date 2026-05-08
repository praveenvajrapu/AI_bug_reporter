import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def test_connection():
    # List available models
    print("Available models:")
    for m in genai.list_models():
        print("-", m.name)

    # Use a supported model (e.g., gemini-pro)
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content("Say hello in one line.")
    print("✅ Gemini connected:", response.text)

if __name__ == "__main__":
    test_connection()