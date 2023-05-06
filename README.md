# This is a private repo for submitting Orr Amsalem's DevOps prject for *DevOpsExperts*

## Preperation
In part 1 of the Project, there are 2 web-servers and a DB connector:
- db_connector.py for connecting to the database and invoking SQL commands
- rest_api.py for the backend web-server
- web_app.py for the frontend web-server with read permissions only.

There are also 3 testing modules as required.

In addition to the required filed for part 1 of the project. I added a script named "clean_db.py"

The script will connect to the DB, clean any existing users table, and recreate the table with 3 users for testing.

The script is design to not interfere with the requested testing modules of the project.
( The script will create users with IDs 1-3, and the testing modules test for users ID >5 )

## Testing
I use **Edge Browser** for selenium testing. Please make sure you update both frontend and combined test modules for your currect Selenim webdriver
