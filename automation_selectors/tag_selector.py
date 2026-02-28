from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    print("Processing...")
    page.goto("https://www.inventory.teamrabbil.com",wait_until="networkidle")

    #tag selector
    tag_element = page.locator("h2").nth(1) # Select the first <h2> element
    tag_text = tag_element.inner_text()
    print(f"Tag Selector Text: {tag_text}")

    #inner html selector
    inner_html_element = page.locator("form").nth(0) # Select the first <form> element
    inner_html = inner_html_element.inner_html()
    print(f"Inner HTML: {inner_html}")

    #attribute selector
    attribute_value = page.locator("input[placeholder='Name']")
    attribute_value.fill("Rabbil") # Fill the input field with the value "Rabbil"

    attribute_value = page.locator("input[placeholder='E-mail']")
    attribute_value.fill("info@rabbil.com") # Fill the input field with the value "Rabbil"

    attribute_value = page.locator("textarea[placeholder='Your Message...']")
    attribute_value.fill("Hi I have a question about your services.") # Fill the input field with the value "Rabbil"
    page.wait_for_timeout(15000)

  

    browser.close()