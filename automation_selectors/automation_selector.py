from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Processing...")
    page.goto("https://www.inventory.teamrabbil.com",wait_until="networkidle")

    #text selector
    # element = page.get_by_text("Login")
    # element.click()
    # print("Current Page Url:", page.url)

    #id selector
    # element = page.locator("#saleBtn")
    # element.click()
    # print("Current Page Url:", page.url)

    #class selector
    element = page.locator(".btn").nth(0) # Get the first element with class "btn"
    text = element.inner_text() # Get the text of the clicked element   
    print(f"Clicked Element Text: {text}")
    element.click()
    print("Current Page Url:", page.url)
    browser.close()