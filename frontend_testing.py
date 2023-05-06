from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(
    service=Service("C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\msedgedriver")
)
url = "http://localhost:5001/users/get_user_data/3"
driver.get(url)
try:
    user_element = driver.find_element(By.ID, value="user")
    if user_element != None:
        print("user name: " + user_element.text)
    else:
        print("No user element found")
except:
    print("User element not found by Selenium")
driver.quit()
