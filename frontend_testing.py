from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(
    service=Service("C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\msedgedriver")
)
url = "http://localhost:5001/users/get_user_data/6"
driver.get(url)
user_element = driver.find_element(By.ID, value="user")
if user_element != None:
    print("user name: " + user_element.text)
else:
    print("No user element found")


# text_option_button = driver.find_element(By.CLASS_NAME, value="VfPpkd-Jh9lGc")
# textfield = driver.find_element(By.XPATH, value="//textarea[@aria-label='Source text']")
# textfield.send_keys("Hello World")
# textfield.send_keys(Keys.ENTER)
# textfield.submit()
# elemList = driver.find_elements(By.CLASS_NAME, value="VfPpkd-Jh9lGc")
# print(len(elemList))
# text_option_button.click()
driver.quit()
