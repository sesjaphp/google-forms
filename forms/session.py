from playwright.sync_api import sync_playwright


class FormSession:
    def __init__(self):
        self.p = None
        self.browser = None
        self.page = None

    def start(self, url: str):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)
        self.page = self.browser.new_page()

        self.page.goto(url)
        self.page.wait_for_timeout(2000)

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.p:
            self.p.stop()
