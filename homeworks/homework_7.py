import sqlite3

connect = sqlite3.connect("my_database.db")

cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    grade INTEGER NOT NULL,
    subject TEXT
    )
''')


def add_student(first_name, last_name, grade, subject):
    cursor.execute(
        "INSERT INTO students(first_name, last_name, grade, subject) VALUES(?,?,?,?)",
        (first_name, last_name, grade, subject)
    )
    connect.commit()
    print("Pupil is added")

def get_students():
    cursor.execute("SELECT first_name, last_name FROM students")
    pupils = cursor.fetchall()
    for pupil in pupils:
        print(f"NAME: {pupil[0]}, SURNAME: {pupil[1]}")

def update_student(student_id=None, new_first_name=None, new_last_name=None):
    if new_first_name:
        cursor.execute(
            "UPDATE students SET first_name = ? WHERE rowid = ?",
            (new_first_name,student_id)
        )
    if new_last_name:
        cursor.execute(
            "UPDATE students SET last_name = ? WHERE rowid = ?",
            (new_last_name,student_id)
        )
    else:
        print("THERE IS NO student with that id")

    connect.commit()
    print("pupil updated")

def delete_student(student_id):
    cursor.execute(f"DELETE FROM students WHERE rowid = {student_id}")
    connect.commit()
    print("pupil deleted")

add_student("Igor","Akinfeef",7,"Physic")
add_student("Arzybek","Kanatbekov",9,"Math")
add_student("Pirigam","Elham",9,"Python")
add_student("Radomir","Nurmuhamedov",9,"Computer science")

get_students()

update_student(2,"Ardager","Ardagerov")

delete_student(1)

get_students()