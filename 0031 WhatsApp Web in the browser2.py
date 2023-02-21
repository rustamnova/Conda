from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime

# Create a new Firefox profile
profile = webdriver.FirefoxProfile()

# Start a new instance of the Firefox driver using the created profile
driver = webdriver.FirefoxProfile()

# Start a new instance of the Firefox driver using the created profile
driver = webdriver.Firefox(firefox_profile=profile)

# Open WhatsApp Web in the browser
driver.get("https://web.whatsapp.com/")

if "session" not in [cookie["name"] for cookie in driver.get_cookies()]:
    # Wait for the user to scan the QR code and log in
    input("Press enter after you have logged in to WhatsApp Web.")
# Check if the "session" cookie is present
else:
    print("You are already logged in.")

# Get the name of the contact from the user
contact_name = input("Enter the name of the contact you want to send a message to: ")

try:
    # Wait for the search bar to be present
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/input/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[3]'))

    )
    search_bar.send_keys(contact_name)
except TimeoutException:
    print("Timed out waiting for the search bar to load")

try:
    # Wait for the desired contact to be present and click on it
    contact = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//span[@title = "{contact_name}"]'))
    )
    contact.click()
except TimeoutException:
    print("Timed out waiting for the send button")
# Wait for the message list to be present
msg_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'message-in')))

# Get the current date
current_date = datetime.now().strftime("%d/%m/%Y")

# Find the messages with the current date
messages_with_current_date = msg_list.find_elements_by_xpath(f'//span[@data-pre-plain-text*="{current_date}"]')

# Print the messages
for message in messages_with_current_date:
    print(message.text)