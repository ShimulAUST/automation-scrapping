from playwright.sync_api import sync_playwright 
import time
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://inventory.teamrabbil.com/DownloadPage",wait_until="networkidle")

    #find the download button and click it
    download_buttons = page.locator("a.btn.btn-success.btn-sm")
    total_files = download_buttons.count()
    print(f"Total files available for download: {total_files}") 

    current_directory = os.getcwd()+"/downloads"
    print(f"Current working directory: {current_directory}")

    for i in range(total_files):
        time.sleep(2)  # Wait for the page to load (adjust the time as needed)
        with page.expect_download() as d:
            download_buttons.nth(i).click()
        
        download = d.value
        fileName = download.suggested_filename
        save_path = os.path.join(current_directory, fileName)
        download.save_as(save_path)

        print(f"File downloaded successfully: {fileName}")
        



    page.click("text=Download All Files")
    browser.close()