import asyncio
from playwright.async_api import async_playwright
import os
import time

async def take_screenshot(url: str):
    """
    Takes a screenshot of the given URL.
    Returns the saved image path.
    """
    # Make sure screenshots folder exists
    os.makedirs("screenshots", exist_ok=True)

    # Unique filename using timestamp
    filename = f"screenshots/screen_{int(time.time())}.png"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()

        try:
            await page.goto(url, timeout=20000, wait_until="networkidle")
        except Exception:
            # If networkidle times out, still take screenshot
            await page.goto(url, timeout=20000)

        await page.screenshot(path=filename, full_page=False)
        await browser.close()

    return filename