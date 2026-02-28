from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Set headless=False to see the browser
    print("Processing...")
    page = browser.new_page()
    page.goto("https://www.shimulpaul.com")
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser
    print(page.title())
    browser.close()