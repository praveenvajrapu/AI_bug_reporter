# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def test_connection():
#     # List available models
#     print("Available models:")
#     for m in genai.list_models():
#         print("-", m.name)

#     # Use a supported model (e.g., gemini-pro)
#     model = genai.GenerativeModel("models/gemini-2.5-flash")
#     response = model.generate_content("Say hello in one line.")
#     print("✅ Gemini connected:", response.text)

# if __name__ == "__main__":
#     test_connection()
import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL.Image

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_screenshot(image_path: str, url: str) -> str:
    """
    Sends screenshot to Gemini Vision.
    Returns raw AI response text.
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    image = PIL.Image.open(image_path)

    prompt = """
    You are a senior QA engineer and UI/UX expert.
    Analyze this website screenshot carefully and identify all visual bugs and UI issues.

    For each bug you find, respond in this EXACT format:

    BUG_START
    title: <short bug title>
    location: <where on the page, e.g. Navbar, Hero Section, Footer>
    severity: <High / Medium / Low>
    description: <1-2 sentence description of the issue>
    fix: <concrete suggestion to fix it>
    BUG_END

    Rules:
    - Only report REAL visible issues you can see in the screenshot
    - Do not make up bugs that aren't visible
    - Severity High = broken functionality or content
    - Severity Medium = bad UX or design issue
    - Severity Low = minor cosmetic issue
    - Find between 3 to 8 bugs maximum
    - If the website looks perfectly fine, report 0 bugs and say "NO_BUGS_FOUND"

    Website URL being analyzed: """ + url + """

    Now analyze the screenshot:
    """

    response = model.generate_content([prompt, image])
    return response.text