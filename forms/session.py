from playwright.async_api import async_playwright

class FormSession:
    def __init__(self):
        self.p = None
        self.browser = None
        self.page = None

    async def start(self, url: str):
        self.p = await async_playwright().start()
        self.browser = await self.p.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        await self.page.goto(url)
        await self.page.wait_for_load_state('domcontentloaded')

    async def stop(self):
        if self.browser:
            await self.browser.close()
        if self.p:
            await self.p.stop()
