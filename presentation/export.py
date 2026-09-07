import asyncio, pathlib
from playwright.async_api import async_playwright
HTML=(pathlib.Path(__file__).parent/"index.html").resolve().as_uri()
OUT=str(pathlib.Path(__file__).parent/"Медиацентр_презентация+кейсы.pdf")
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto(HTML); await pg.emulate_media(media="print")
        try: await pg.wait_for_function("document.fonts.ready",timeout=4000)
        except Exception: pass
        await pg.wait_for_timeout(600)
        await pg.pdf(path=OUT,width="1280px",height="720px",print_background=True,prefer_css_page_size=True)
        await b.close(); print("PDF →",OUT)
asyncio.run(main())
