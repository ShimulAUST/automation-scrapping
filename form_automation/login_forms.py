from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    #auto login form
    page.goto("http://www.inventory.teamrabbil.com/userLogin",wait_until="networkidle")
    page.locator("#email").fill("hello01@gmail.com") # Fill the email field with the value "
    page.locator("#password").fill("password123") # Fill the password field with the value "password123" 

    #waiting
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Next",exact=False).click() # Click the "Login" button to submit the form   

    #goto profile page and update profile
    page.goto("http://www.inventory.teamrabbil.com/userProfile",wait_until="networkidle")
    page.wait_for_timeout(5000)

    page.locator("#firstName").fill("") # Fill the first name field with the value "Shimul1" 
    page.locator("#lastName").fill("") # Fill the last name field with the value "Paul1"

    page.wait_for_timeout(5000)

    page.locator("#firstName").fill("Shimul2") # Fill the first name field with the value "Shimul2" 
    page.locator("#lastName").fill("Paul2") #  Fill the last name field with the value "Paul2"


    page.get_by_text("Update",exact=False).click() # Click the "Update Profile" button to submit the form
    page.wait_for_timeout(5000)

    
    page.goto("http://inventory.teamrabbil.com/dashboard",wait_until="networkidle") # Load the dashboard page after profile update
    page.wait_for_timeout(5000)

    page.goto("http://inventory.teamrabbil.com/logout",wait_until="networkidle") # Navigate to the login page after logout
    page.wait_for_timeout(5000)

    print("Current Page Url:", page.url) # Print the current page URL after form submission
    browser.close()
