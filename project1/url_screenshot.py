from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.google.com",wait_until="networkidle") # Navigate to GitHub

     # Take a screenshot of the GitHub page
    page.screenshot(path="screenshot.png", full_page=True)
    print("Screenshot taken: screenshot.png")

    browser.close()