from playwright.async_api import async_playwright

async def get_products():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.daraz.pk/smartphones/")
        await page.wait_for_selector('div[data-qa-locator="product-item"]')
        titles = await page.locator('div[data-qa-locator="product-item"] > div > a').all_inner_texts()
        return titles