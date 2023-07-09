# from unittest import TestCase
import requests

# Setting some variables for easy testing
userName = "docker test user"
userID = "50"
url = f"http://localhost:5000/users/{userID}"
jsonBody = {"user_name": f"{userName}"}

# POST request test
post = requests.post(url=url, json=jsonBody)
if post.status_code == 200:
    res = post.json()
    if res["user_added"] == userName:
        print("User Created Successfully")
        exit(0)
elif post.status_code == 500:
    print("User ID already in use")
    exit(1)
else:
    print("POST request failed")
    exit(1)

# Test successful user creation by querying the DB
get = requests.get(url=url)
if get.status_code == 200:
    res = get.json()
    if res["user_name"] == userName:
        print("User creation is validated")
        exit(0)
    elif res["user_name"] != userName:
        print("The user id in the database belongs to a defferent user")
        exit(0)
elif get.status_code == 500:
    print("User validation failed. ID does not exist in the database")
    exit(1)
else:
    print("GET request failed")
    exit(1)
