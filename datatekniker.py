import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

async def interact_with_elements(driver, wait):
    # Interact with elements using provided XPaths with added wait conditions
    xpaths = []
    for i in range(2, 12):  # Generate XPaths from index 2 to 11
        xpath = '//*[@id="resultater"]/div[1]/div/div[' + str(i) + ']/div[1]/div[1]/span/h3'
        xpaths.append(xpath)

    # List to store company names and corresponding emails
    company_emails = []

    for xpath in xpaths:
        try:
            element = await asyncio.to_thread(lambda: wait.until(EC.visibility_of_element_located((By.XPATH, xpath))))
            # Perform actions on each element, for example, printing its text
            print("Element text:", element.text)
            VirksomhedsNavn = element.text
            element.click()
            # Get the text of the desired XPath
            retry_count = 0
            while retry_count < 5:
                try:
                    # Extract email from the page
                    email_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div[1]/table/tbody/tr[5]')
                    email = email_element.text.split(':')[-1].strip()  # Assuming email is the last item after ':'
                    print("Email found:", email)
                    # Append company name and email to the list if email is found
                    company_emails.append((VirksomhedsNavn, email))
                    # Go back to the previous page
                    driver.back()
                    await asyncio.sleep(1)  # Wait for a second before searching again
                    break  # Exit the loop once found and gone back
                except NoSuchElementException:
                    print("Email not found, continuing search...")
                    retry_count += 1
            else:
                print("Email not found after 5 attempts, continuing to the next XPath...")
                driver.back()
        except TimeoutException:
            print("Timeout occurred while waiting for element with XPath:", xpath)
            continue  # Continue to the next XPath if timeout occurs
    return company_emails

async def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Waiting for {remaining} seconds...")
        await asyncio.sleep(1)

async def main():
    #chrome
    driver = webdriver.Chrome()

    #Mit_it can be removed, so it automaticly just goes to {pages} and take it from there, but the fact ialready has this, it can goto soeglog, but its up to the user of choice.
    driver.get("https://www.laerepladsen.dk/")

    # Wait for the body tag to be present
    wait = WebDriverWait(driver, 30)
    await asyncio.to_thread(lambda: wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))))

    # Find and interact with the button using XPath
    log_ind_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/header/div/div/button')
    log_ind_button.click()

    log_med_MitID = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/main/div/div/div[2]/div[1]/div/button[2]')
    log_med_MitID.click()

    # Wait until the URL changes to the desired URL or its redirected URL
    expected_urls = [
        "https://pms.laerepladsen.dk/elev-index",
        "https://pms.laerepladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering"
    ]

    while True:
        current_url = driver.current_url
        print("Current URL:", current_url)
        if current_url in expected_urls:
            if current_url == expected_urls[1]:
                print("Redirected to the desired page.")
            break
        await asyncio.sleep(1)

    # Proceed with the rest of the process
    print("Starting data extraction...")

    # Interaction with elements and clicking the button repeatedly
    virksomheds_with_emails = set()  # Set to store unique company names with emails
    for page_num in range(51):  # Iterate from 0 to 50
        print("Current page:", page_num)
        # Interact with elements
        company_emails = await interact_with_elements(driver, wait)

        # Save company names with corresponding emails
        for company_name, email in company_emails:
            if email:
                virksomheds_with_emails.add(company_name)

        # Save emails to a text file for this page
        page_filename = f'page_{page_num}_emails.txt'
        print(f"Saving emails to a text file for page {page_num}...")
        
        with open(page_filename, 'w') as f:
            for _, email in company_emails:
                if email:
                    f.write(email + '\n')
        print(f"Emails saved to {page_filename}")

        # Start countdown timer
        await countdown_timer(3)

        # Go to the next page
        try:
            next_page_url = f"https://pms.laerepladsen.dk/soeg-opslag/{page_num}/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=0a3f50bd-fbe3-32b8-e044-0003ba298018"
            print("Next page URL:", next_page_url)
            await asyncio.to_thread(lambda: driver.get(next_page_url))
            await asyncio.to_thread(lambda: wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))))
        except TimeoutException:
            print("Timeout exception: Page did not load within the specified time.")
        except Exception as e:
            print("An error occurred:", e)
            break

    # Save the list of companies with emails to the virksomheds.txt file
    with open('virksomheds.txt', 'w') as f:
        for company_name in virksomheds_with_emails:
            f.write(company_name + '\n')

    # Close the browser window when you're done
    driver.quit()

# Run the asyncio loop
asyncio.run(main())
