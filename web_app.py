from flask import Flask, request
import db_connector as db
import os
import signal

app = Flask(__name__)
htmlHelpFile = (
    "C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\Project-Part1\\web_app.html"
)


@app.route("/", methods=["GET"])
def root():
    return "web-server is online", 200


# Testing assignment extra tasks for generating documentation html files
@app.route("/help", methods=["GET"])
def help():
    with open(htmlHelpFile, "r") as o:
        content = o.read()
        return content, 200


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


@app.route("/stop_server")
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return "Server stopped"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5001)
