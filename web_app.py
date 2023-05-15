from flask import Flask, request
import rest_api
import db_connector as db

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "web-server is online", 200


@app.route("/help", methods=["GET"])
def help():
    with open(
        "C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\Project-Part1\\web_app.html", "r"
    ) as o:
        content = o.read()
        return content, 200


##### a test route for getting data using Rest_API Module #####

# @app.route("/users/get_user_data/<user_id>", methods=["GET"])
# def get_user_data(user_id):
#     uName = rest_api.get_user(user_id)[0].get("user_name")
#     if uName == None:
#         return f"<H1 id='error'> No such user {user_id}</H1>"
#     elif uName != None:
#         return f"<H1 id='user'>{uName}</H1>"


# app.run(host="127.0.0.1", debug=True, port=5001)


#############################


########## Getting data directly from DB ##########


@app.route("/users/get_user_data/<user_id>", methods=["GET"])
def getUserData(user_id):
    uName = db.get_user_data(user_id)
    if uName == None:
        return f"<H1 id='error'>No such user: {user_id}</H1>"
    else:
        return f"<H1 id='user'>{uName}</H1>"


## Route for deleting the table form the database
# @app.route("/users/drop", methods=["GET"])
# def drop_db():
#     db.drop_table()
#     return "Table deleted", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5001)
