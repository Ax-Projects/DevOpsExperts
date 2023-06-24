import pymysql
import datetime
import os

schema_name = "devopsdb"

# These are private variables for ease of update if the database connection changes.
# I have not found a way to use a pymysql.connect function without calling it directly in each of my functions.
_host = "localhost"
_user = "devopsroot"
_password = "r83nHqs7wew9Gycr"
_db = "devopsdb"
_port = 3306


def dbconn():
    conn = pymysql.connect(
        host=_host,
        user=_user,
        password=_password,
        db=_db,
        port=_port,
    )
    try:
        yield conn
    except pymysql.ConnectionError as e:
        print("Connection error: %s" % e)


def get_dbconn():
    pymysql.connect(
        host=_host,
        user=_user,
        password=_password,
        db=_db,
        port=_port,
    )


def check_table_exists():
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_schema = '{schema_name}' AND table_name = 'users' LIMIT 1;"
        )
        if (
            "users" in cursor.fetchone()
        ):  # This is a dumb workaround to check if the table exists by checking the cursor returned values
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False
    # except pymysql.Error as e:
    except Exception as e:
        conn.close()
        return e


# Inserting data into table
def create_table():
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        statementToExecute = f"CREATE TABLE `{schema_name}`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL,`creation_date` VARCHAR(50) NOT NULL, PRIMARY KEY (`user_id`));"
        cursor.execute(statementToExecute)
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        # print(e)
        return e


# Getting users table from the Database
def get_users():
    conn = dbconn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.users;")
    output = cursor.fetchall()
    cursor.close()
    conn.close()
    return output


def get_user_data(user_id: str):
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT user_name FROM {schema_name}.users WHERE user_id = {user_id};"
        )
        output = cursor.fetchone()
        cursor.close()
        conn.close()
        return output[0]
    except pymysql.Error as e:
        return e
    except TypeError as e:
        return None


# Inserting data into table
def create_user(user_id: str, user_name: str):
    timenow = str(datetime.datetime.now()).split(".")[0]
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT into {schema_name}.users (user_name, user_id, creation_date) VALUES ('{user_name}', '{user_id}', '{timenow}');"
        )
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        return e


# Updating data in the table
def update_user(user_id: str, user_name: str):
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE {schema_name}.users SET user_name = '{user_name}' WHERE user_id = '{user_id}'"
        )
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        return e


# Deleting the data from the table
def delete_user(user_id: str):
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        return e


# Function for dropping the table
def drop_table():
    try:
        conn = dbconn()
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE `{schema_name}`.`users`;")
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        return e
