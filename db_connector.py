import pymysql
import datetime
import os


DBHOST = "localhost"
DBUSER = "devopsroot"
DBPASSWORD = "r83nHqs7wew9Gycr"
DB = "devopsdb"
SCHEMA = "devopsdb"
PORT = 3306


def db():
    conn = pymysql.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASSWORD,
        db=DB,
        # port=_port,
    )
    conn.autocommit(True)
    return conn


schema_name = SCHEMA


def check_table_exists():
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_schema = '{schema_name}' AND table_name = 'users' LIMIT 1;"
        )
        if (
            cursor.fetchone()
        ):  # This is a dumb workaround to check if the table exists by checking the cursor returned values
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False
    except pymysql.Error as e:
        conn.close()
        return {e}


# Inserting data into table
def create_table():
    try:
        conn = db()
        cursor = conn.cursor()
        statementToExecute = f"CREATE TABLE `{schema_name}`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL,`creation_date` VARCHAR(50) NOT NULL, PRIMARY KEY (`user_id`));"
        cursor.execute(statementToExecute)
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        # print(e)
        cursor.close()
        conn.close()
        return {e}


# Getting users table from the Database
def get_users():
    conn = db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.users;")
    output = cursor.fetchall()
    if output:
        cursor.close()
        conn.close()
        return output
    else:
        cursor.close()
        conn.close()
        return None


def get_user_data(user_id: str):
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT user_name FROM {schema_name}.users WHERE user_id = {user_id};"
        )
        output = cursor.fetchone()
        if output:
            cursor.close()
            conn.close()
            return output[0]
        else:
            cursor.close()
            conn.close()
            return None
    except pymysql.Error as e:
        cursor.close()
        conn.close()
        return {e}
    except TypeError as e:
        cursor.close()
        conn.close()
        return None


# Inserting data into table
def create_user(user_id: str, user_name: str):
    timenow = str(datetime.datetime.now()).split(".")[0]
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT into {schema_name}.users (user_name, user_id, creation_date) VALUES ('{user_name}', '{user_id}', '{timenow}');"
        )
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        cursor.close()
        conn.close()
        return {e}
    # except pymysql.Error as e:
    #     return {e}


# Updating data in the table
def update_user(user_id: str, user_name: str):
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE {schema_name}.users SET user_name = '{user_name}' WHERE user_id = '{user_id}'"
        )
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        cursor.close()
        conn.close()
        return {e}


# Deleting the data from the table
def delete_user(user_id: str):
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        cursor.close()
        conn.close()
        return {e}


# Function for dropping the table
def drop_table():
    try:
        conn = db()
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE `{schema_name}`.`users`;")
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        cursor.close()
        conn.close()
        return {e}
