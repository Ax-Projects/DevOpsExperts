from flask import Flask, request

app = Flask(__name__)

# local users storage
users: dict = {}


@app.route("/", methods=["GET"])
def root():
    return "server is online", 200


@app.route("/users/<user_id>", methods=["GET", "POST", "DELETE", "PUT"])
def user(user_id):
    if request.method == "GET":
        # Error catching in GET request for user name by user_id
        try:
            # Checking if user_id exists in users dictionary
            if users.get(user_id):
                return {"status": "OK", "user_name": users[user_id]}, 200
            else:
                return {"status": "error", "reason": "no such id"}, 500
        # Catching KeyError type error and printing to terminal
        except Exception as e:
            print(f"Error in GET method: {e}")

    elif request.method == "POST":
        # getting the json data payload from request
        request_data = request.json
        # Checking if user_id exists in users dictionary
        if users.get(user_id):
            return {"status": "error", "reason": "ID already exists"}, 500
        else:
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get("user_name")
            users[user_id] = user_name
            return {"status": "OK", "user_added": user_name}, 200

    elif request.method == "PUT":
        # getting the json data payload from request
        request_data = request.json
        # Checking if user_id exists in users dictionary
        if users.get(user_id):
            users[user_id] = request_data.get("user_name")
            return {"status": "OK", "user_updated": users[user_id]}, 200
        else:
            # treating request_data as a dictionary to get a specific value from key
            return {"status": "error", "reason": "No such ID"}, 500

    elif request.method == "DELETE":
        # Error catching in DELETE request for user name by user_id
        try:
            # Checking if user_id exists in users dictionary
            if users.get(user_id):
                users.pop(user_id)
                return {"status": "OK", "user_deleted": user_id}, 200
            else:
                return {"status": "error", "reason": "no such id"}, 500
        # Catching KeyError type error and printing to terminal
        except Exception as e:
            print(f"Error in DELTE method: {e}")


app.run(host="127.0.0.1", debug=True, port=5000)
