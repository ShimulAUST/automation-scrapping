from playwright.sync_api import sync_playwright
import time 
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://www.inventory.teamrabbil.com/userLogin",wait_until="networkidle")
    page.locator("#email").fill("hello01@gmail.com") # Fill the email field with the value "
    page.locator("#password").fill("password123") # Fill the password field with the value "password123" 

    #waiting
    with page.expect_navigation(wait_until="networkidle"):
        page.get_by_text("Next",exact=False).click() # Click the "Login" button to submit the form   
    
    print("login successful!")

    #customer page
    page.goto("http://www.inventory.teamrabbil.com/customerPage",wait_until="networkidle")


    #read customer data
    with open("customer.csv",newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["customerName"]
            email = row["customerEmail"]
            mobile = row["customerMobile"]

            #oper the modal
            page.locator("button[data-bs-target='#create-modal']").click()
            page.wait_for_timeout(2000)

            #fill the form
            page.locator("#customerName").fill(name)
            page.locator("#customerEmail").fill(email)
            page.locator("#customerMobile").fill(mobile)

            page.wait_for_timeout(1000)

            #submit the form
            page.locator("#save-btn").click()
            page.wait_for_timeout(1000)
            print(f"Customer added successfully: {name}")
        
    browser.close()