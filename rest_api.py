import requests

operation = True


def test():
    task = input(
        "This is a test sscript for REST requests.\nPlease enter a REST method you want to test (get, post, put, delete)\nTo exit the script write 'exit'\n"
    ).lower()
    return task


task = test()
while operation == True:
    if task == "get":
        res = requests.get("http://127.0.0.1:5000/users/1")
        if res.ok:
            print(res.json())
        else:
            task = test()
            break
    elif task == "post":
        res = requests.post(
            "http://127.0.0.1:5000/users/1", json={"user_name": "Orr Amsalem"}
        )
        if res.ok:
            print(res.json())
        else:
            task = test()
            break
    elif task == "put":
        res = requests.put(
            "http://127.0.0.1:5000/users/1", json={"user_name": "John Smith"}
        )
        if res.ok:
            print(res.json())
    elif task == "delete":
        res = requests.delete("http://127.0.0.1:5000/users/1")
        if res.ok:
            print(res.json())
    elif task == "exit":
        operation = False
    else:
        print(
            "You must provide one of the following input parameters: get, post, put or delete"
        )
