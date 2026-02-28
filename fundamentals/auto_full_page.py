from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Processing...")
    page.goto("https://www.shimulpaul.com",wait_until="networkidle")
    content = page.content()
    with open("page_content.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Page content saved to page_content.html")
    browser.close()