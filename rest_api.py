from flask import Flask, request
import db_connector as db
import os
import signal

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "server is online", 200


@app.route("/users/<user_id>", methods=["GET", "POST", "DELETE", "PUT"])
def user(user_id):
    if request.method == "GET":
        # Error catching in GET method for user name by user_id
        try:
            # get_user(uid=str(user_id))   # attempt at exporting the functionality to global scope funciton
            userData = db.get_user_data(str(user_id))
            if userData != None:
                return {"status": "OK", "user_name": userData}, 200
            elif userData == None:
                return {"status": "error", "reason": "no such id"}, 500
        # Catching Exception type error and printing to terminal
        except Exception as e:
            print(f"Error in GET method:\n {e}")

    elif request.method == "POST":
        # Error catching for POST method
        try:
            # getting the json data payload from request
            request_data = request.json
            # Checking if user_id exists in the DB
            userData = db.get_user_data(user_id)
            if userData != None:
                return {"status": "error", "reason": "ID already exists"}, 500
            else:
                # Checking if the Json payload contains user_name
                try:
                    user_nm = request_data.get("user_name")
                except:
                    user_nm = None
                if user_nm is not None:
                    # Using DB method to create a new user
                    status = db.create_user(user_id=user_id, user_name=user_nm)
                    # Checking DB method result
                    if status == True:
                        return {"status": "OK", "user_added": user_nm}, 200
                    else:
                        return {f"error": status}, 400
                elif user_nm == None:
                    print(
                        "user_name is not specified in the POST request's payload"
                    )  # Print if JSON payload doesn't contain user_name
        except Exception as e:
            print(f"Error in  POST method:\n {e}")

    elif request.method == "PUT":
        try:
            request_data = request.json
            # Checking if user_id exists in the DB
            userData = db.get_user_data(user_id)
            if userData == None:
                return {"status": "error", "reason": "No such ID"}, 500
            elif userData != None:
                newUserName = request_data.get("user_name")
                status = db.update_user(user_id=userData, user_name=newUserName)
                if status == True:
                    return {"status": "OK", "user_updated": userData}, 200
                else:
                    return {f"sql error": status}, 400
            else:
                return {"status": "error", "reason": status}, 400
        except Exception as e:
            print(f"Error in  PUT method:\n {e}")

    elif request.method == "DELETE":
        # Error catching in DELETE request for user name by user_id
        try:
            userData = db.get_user_data(user_id)
            if userData == None:
                return {"status": "error", "reason": "no such id"}, 500
            else:
                status = db.delete_user(user_id)
                if status == True:
                    return {"status": "OK", "user_deleted": user_id}, 200
                else:
                    return {"sql error": status}, 400
        except Exception as e:
            print(f"Error in DELETE method:\n {e}")


@app.route("/stop_server")
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return "Server stopped"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5000)
