from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()       
    page.goto("https://www.google.com") # Navigate to Google
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser

    # You can also navigate to another URL
    page.goto("https://www.github.com") # Navigate to GitHub
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser

    # You can also navigate to another URL
    page.goto("https://www.shimulpaul.com")  # Navigate to Shimul Paul's website
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser


    page.reload()  # Reload the current page
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser

    page.go_back()  # Go back to the previous page (GitHub)
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser

    page.go_back()  # Go back to the previous page (Google)
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the    

    page.go_forward()  # Go forward to the next page (GitHub)
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser 

    page.go_forward()  # Go forward to the next page (Shimul Paul's website)
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the browser
    
    browser.close()