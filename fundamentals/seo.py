from  playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.rabbil.com",wait_until="networkidle")  # Navigate to Rabbil's website

    title = page.locator("title").first.inner_text() # Get the title of the page
    print(f"Page Title: {title}")

    description = page.locator("meta[name='description']").get_attribute("content") # Get the meta description
    print(f"Meta Description: {description}")

    keywords = page.locator("meta[name='keywords']").get_attribute("content") # Get the meta keywords
    print(f"Meta Keywords: {keywords}") 

    browser.close()