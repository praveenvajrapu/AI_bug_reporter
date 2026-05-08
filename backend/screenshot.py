import asyncio
from playwright.async_api import async_playwright
import os

async def take_screenshot(url: str, save_path: str = "screenshots/screen.png"):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto(url, timeout=15000)
        await page.screenshot(path=save_path, full_page=False)
        await browser.close()
        print(f"✅ Screenshott saved: {save_path}")
        return save_path

# Test it
if __name__ == "__main__":
    asyncio.run(take_screenshot("https://www.python.org"))