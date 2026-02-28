from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    #viewport
    page.set_viewport_size({"width": 414 , "height": 896})
    page.goto("https://www.shimulpaul.com",wait_until="networkidle")
    page.screenshot(path="viewport.png", full_page=True)
    print("Screenshot taken: viewport_mobile.png")
    browser.close()