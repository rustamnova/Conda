from selenium import webdriver

# Start a new instance of the Firefox driver
driver = webdriver.Firefox()

# Open WhatsApp Web in the browser
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code and log in
input("Press enter after you have logged in to WhatsApp Web.")

# Find the search bar and send the desired contact's name
search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
search_bar.send_keys("John Smith")

# Find and click on the desired contact
contact = driver.find_element_by_xpath('//span[@title = "John Smith"]')
contact.click()

# Find the message box and send the message
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msg_box.send_keys("Hello, John! How are you?")

# Find and click on the send button
send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
send_button.click()

# Close the browser
driver.quit()
