from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_update(username, password):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:
        # Open the hh.ru login page
        driver.get("https://hh.ru/account/login?backurl=%2F&hhtmFrom=main")

        # Switch to password login
        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="expand-login-by-password"]').click()

        # Input username and password
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-input-username"]').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-input-password"]').send_keys(password)

        # Click the log in button
        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="account-login-submit"]').click()

        # Wait for the element to appear after login
        wait = WebDriverWait(driver, 10)
        myresumes = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-qa="mainmenu_myResumes"]')))
        myresumes.click()

        # Click the resume update button
        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="resume-update-button_actions"]').click()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

# Provide your hh.ru credentials here
username = ""
password = ""

# Call the function to log in and click the resume update button
login_and_update(username, password)