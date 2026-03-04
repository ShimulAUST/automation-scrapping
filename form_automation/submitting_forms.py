from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navigate to the target website page
    page.goto("https://www.inventory.teamrabbil.com/userRegistration",wait_until="networkidle")  


    page.locator("#email").fill("hello01@gmail.com") # Fill the email field with the value "
    page.locator("#firstName").fill("Shimul") # Fill the first name field with the value "Rabbil"
    page.locator("#lastName").fill("Paul") # Fill the last name field with the value "Paul"
    page.locator("#mobile").fill("01700000000") # Fill the mobile field with the value "01700000000"
    page.locator("#password").fill("password123") # Fill the password field with the value "password123"    
    
    #waiting
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Complete").click() # Click the "Complete" button to submit the form

    print("Form submitted successfully!")
    print("Current Page Url:", page.url) # Print the current page URL after form submission 
    browser.close()
