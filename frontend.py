# from flask import Flask, request
# import db_connector
import rest_api

# users = db_connector.get_users()
# print(users)
# db_connector.create_user(user_id="7", user_name="Sarah")

uName = rest_api.get_user("4")[0].get("user_name")
print(uName)
