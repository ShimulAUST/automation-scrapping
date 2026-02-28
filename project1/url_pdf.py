from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.shimulpaul.com",wait_until="networkidle") # Navigate to Shimul Paul's website

    #get the PDF content of the page
    page.pdf(path="page.pdf", format="A4",print_background=True)  
    print("PDF saved: page.pdf")
    browser.close()