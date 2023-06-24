import db_connector_host as db


def create_table_with_users():
    try:
        createTable = db.create_table()
        if createTable == True:
            print("Table created successfully")
            # Create a few new users
            users = ["Orr", "Tal", "Tom"]
            id = 1
            for user in users:
                db.create_user(user_id=id, user_name=user)
                id += 1
            print("Users added to database")
            exit(0)
        else:
            print("Creating new users table failed")
            print(createTable)
    except Exception as e:
        print(e)


# Check if db exists
result = db.check_table_exists()
if result == False:
    print("Table not found. Creating a new one")
    create_table_with_users()

# If db exists, drop the users table
elif result == True:
    dropTable = db.drop_table()
    if dropTable != True:
        print("Dropping table Failed")
        exit(1)
    # If table dropped successfully, create a new users table and insert some users
    elif dropTable == True:
        print("Old users table dropped successfully. Creating new users table")
        create_table_with_users()
