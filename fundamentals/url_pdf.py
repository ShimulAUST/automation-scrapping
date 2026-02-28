from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.daraz.com.bd",wait_until="networkidle") # Navigate to Daraz   website

    #get the PDF content of the page
    page.pdf(path="page.pdf", format="A4",print_background=True)  
    print("PDF saved: page.pdf")
    browser.close()