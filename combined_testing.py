import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# Setting some variables for easy testing
userName = "combined test user"
userID = "10"
url = f"http://localhost:5000/users/{userID}"
jsonBody = {"user_name": f"{userName}"}

# POST request test
post = requests.post(url=url, json=jsonBody)
if post.status_code == 200:
    # Test successful user creation by using GET
    get = requests.get(url=url)
    if get.status_code == 200:
        res = get.json()
        if res["user_name"] == userName:
            print("User creation is validated")
        elif res["user_name"] != userName:
            print("The user id in the database belongs to a defferent user")
    elif get.status_code == 500:
        print("User validation failed. ID does not exist in the database")
    else:
        print("GET request failed")
elif post.status_code == 500:
    print("User ID already in use")
else:
    print("POST request failed")


# Check if the user exists in the database directly
try:
    conn = pymysql.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7615057",
        password="nUYs7WA6Mx",
        db="sql7615057",
        port=3306,
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT user_name FROM sql7615057.users WHERE user_id = {userID};")
    output = cursor.fetchone()
    cursor.close()
    conn.close()
    print(output)
    ### Pretty print
    # print(output[0])
except pymysql.Error as e:
    print(e)

# Comparing the results
if output[0] == userName:
    print("User retrieved successfully from database")

# Validating the results with Selenium
driver = webdriver.Edge(
    service=Service("C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\msedgedriver")
)
url = f"http://localhost:5001/users/get_user_data/{userID}"
try:
    driver.get(url)
    user_element = driver.find_element(By.ID, value="user")
    if user_element.text == userName:
        print("user validated successfully using web browser")
        print("user name: " + user_element.text)
    elif user_element.text != userName:
        print("The user name is incorrect, belongs to a different user")
    else:
        print("No user element found")
except:
    print("User element not found by Selenium")
driver.quit()
