import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

async def run():
    # use the root index.html file
    html_path = Path('index.html').resolve()
    pdf_path = Path('index_playwright_v2.pdf').resolve()
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(html_path.as_uri())
        await page.pdf(path=str(pdf_path), format='A4', print_background=True)
        await browser.close()
    print('PDF generated at', pdf_path)

if __name__ == '__main__':
    asyncio.run(run())
