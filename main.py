from playwright.sync_api import sync_playwright
import webbrowser

def extraer_info(data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto('https://www.justwatch.com/')

            search_bar = page.locator('input[aria-label="search text"]')
            search_bar.wait_for()
            search_bar.fill(data)
            search_bar.press('Enter')
            page.wait_for_load_state('networkidle')
            headers_locator = page.locator('span.header-title')
            headers_texts = headers_locator.all_text_contents()
            headers_links = page.locator('a.href')
            print(headers_texts)

        finally:

            browser.close()


extraer_info(input('pone una peli aca: '))