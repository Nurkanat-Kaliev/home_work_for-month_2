import sqlite3

# A4
connect = sqlite3.connect("users.db")

# hand with pan
cursor = connect.cursor()

cursor.execute('''
       CREATE TABLE IF NOT EXISTS users(
       name VARCHAR (100) NOT NULL,
       age INTEGER NOT NULL,
       hobby TEXT
       )
''')

connect.commit()
# CRUD create read update delete

def add_user(name,age,hobby):
    # cursor.execute(f'INSERT INTO users(name,age,hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        "INSERT INTO users(name,age,hobby) VALUES(?,?,?)",
        (name,age,hobby)
    )
    connect.commit()
    print("user is added")

# add_user("geroy",23,"football")

def get_user():
    cursor.execute('SELECT name,age,hobby FROM users')
    users = cursor.fetchall()
    for user in users:
        print(f'name: {user[0]}, age: {user[1]}, hobby: {user[2]}')


# get_user()

def update_user(name=None,age=None,hobby=None,row_id=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name,row_id)
        )
    if age:
            cursor.execute(
                'UPDATE users SET age = ? WHERE rowid = ?',
                (age, row_id)
            )
    if hobby:
            cursor.execute(
                'UPDATE users SET hobby = ? WHERE rowid = ?',
                (hobby, row_id)
            )
    connect.commit()
    print("user is updated")

update_user("Arzybekov",45,"volleyball",1)

# get_user()

# def delete_users(row_id):
#     cursor.execute(f'DELETE FROM users WHERE rowid = "{row_id}"')
#
#     connect.commit()
#     print("user is deleted")
#
# delete_users(1)
# delete_users(2)
get_user()


