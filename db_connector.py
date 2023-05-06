import pymysql
import datetime

schema_name = "sql7615057"


def check_table_exists():
    try:
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(
            """
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = 'users'
        """
        )
        if cursor.fetchone()[0] == 1:
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False
    except pymysql.Error as e:
        conn.close()
        return e


# Inserting data into table
def create_table():
    try:
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
        conn.autocommit(True)
        cursor = conn.cursor()
        statementToExecute = f"CREATE TABLE `{schema_name}`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL,`creation_date` VARCHAR(50) NOT NULL, PRIMARY KEY (`id`));"
        cursor.execute(statementToExecute)
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        # print(e)
        return e


# Getting users table from the Database
def get_users():
    conn = pymysql.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7615057",
        password="nUYs7WA6Mx",
        db="sql7615057",
        port=3306,
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.users;")
    output = cursor.fetchall()
    cursor.close()
    conn.close()
    return output


def get_user_data(user_id: str):
    try:
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
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
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
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
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
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
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
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
        conn = pymysql.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7615057",
            password="nUYs7WA6Mx",
            db="sql7615057",
            port=3306,
        )
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE `{schema_name}`.`users`;")
        cursor.close()
        conn.close()
        return True
    except pymysql.Error as e:
        return e
