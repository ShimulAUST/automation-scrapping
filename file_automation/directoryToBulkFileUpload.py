import os
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com/public/UploadPage",wait_until="networkidle")
    

    for fileName in os.listdir("images"):
        filePath = os.path.join("images", fileName)
        page.set_input_files("input[name='file']", filePath)
        page.click("button[type='submit']")

        #check if the file is uploaded successfully

        try:
            page.wait_for_selector(".alert-success", timeout=5000)  # Wait for the success alert to appear on the page
            print(f"File uploaded successfully: {fileName}")
        except:
            print(f"Failed to upload file: {fileName}")
        time.sleep(5)  # Wait for 5 seconds before uploading the next file
        page.reload(wait_until="networkidle")  # Reload the page to reset the form for the next upload

    browser.close()
    print("All files processed.")