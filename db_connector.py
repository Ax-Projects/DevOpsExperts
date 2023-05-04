import pymysql

conn = pymysql.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7615057",
    password="nUYs7WA6Mx",
    db="sql7615057",
    port=3306,
)
conn.autocommit(True)
cursor = conn.cursor()

schema_name = "sql7615057"


def check_Table():
    cursor.execute(
        """
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'users'
    """
    )
    if cursor.fetchone() is not None:
        return 1
    else:
        return 0


# f"IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{schema_name}' AND  TABLE_NAME = 'users'))"

print(check_Table())
# cursor.execute(
#     f"IF OBJECT_ID (N'users', N'U') IS NOT NULL SELECT 1 AS res ELSE SELECT 0 AS res;"
# )
# Creating users table in the Database
# if check_Table() == False:
#     try:
#         statementToExecute = f"CREATE TABLE `{schema_name}`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL, `creation_date` VARCHAR(50) NOT NULL, PRIMARY KEY (`user_id`));"
#         cursor.execute(statementToExecute)
#     except Exception as e:
#         print(e)


# def get_users():
#     cursor.execute(f"SELECT * FROM {schema_name}.users;")
#     for row in cursor:
#         print(row)


# # Inserting data into table
# cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('Orr', 30)")
# get_users()

# # Instering More users
# cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('Tal', 2)")
# cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('Roey', 5)")

# # Getting users from the table
# cursor.execute(f"SELECT * FROM {schema_name}.users;")
# for row in cursor:
#     print(row)

# # Updating data in the table
# cursor.execute(f"UPDATE {schema_name}.users SET id = '10' WHERE name = 'Orr'")
# cursor.execute(f"UPDATE {schema_name}.users SET name = 'Roey-Shmu' WHERE id = '5'")

# # Deleting the data from the table
# cursor.execute(f"DELETE FROM {schema_name}.users WHERE name = 'Orr'")
# get_users()


cursor.execute(f"DROP TABLE `{schema_name}`.`users`;")

cursor.close()
conn.close()
