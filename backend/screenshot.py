import asyncio
from playwright.async_api import async_playwright
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)
async def take_screenshot(url: str):
    os.makedirs("screenshots", exist_ok=True)
    filename = f"screen_{int(time.time())}.png"
    local_path = f"screenshots/{filename}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        try:
            await page.goto(url, timeout=20000, wait_until="networkidle")
        except Exception:
            await page.goto(url, timeout=20000)

        # ✅ Fixed — use local_path not filename
        await page.screenshot(path=local_path, full_page=False)
        await browser.close()

    result = cloudinary.uploader.upload(
        local_path,
        folder="ai-bug-reporter",
        public_id=filename.replace(".png", ""),
        resource_type="image"
    )

    # ✅ Return both — local path for Gemini, URL for frontend
    return local_path, result["secure_url"]