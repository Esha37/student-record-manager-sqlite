#Student record manager CLI 
#data base 

import sqlite3

# Database Connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Create Table
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        marks INTEGER,
        grade TEXT
    )
    """)
    conn.commit()


# Calculate Grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


# Add Student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = int(input("Enter student marks: "))

    grade = calculate_grade(marks)

    cursor.execute(
        "INSERT INTO students(name, age, marks, grade) VALUES (?, ?, ?, ?)",
        (name, age, marks, grade)
    )

    conn.commit()

    print("Student added successfully!")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== Student Records =====")

    for student in students:
        print("---------------------------")
        print("ID    :", student[0])
        print("Name  :", student[1])
        print("Age   :", student[2])
        print("Marks :", student[3])
        print("Grade :", student[4])


# Search Student
def search_student():
    search_name = input("Enter student name to search: ")

    cursor.execute(
        "SELECT * FROM students WHERE LOWER(name) = LOWER(?)",
        (search_name,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("---------------------------")
        print("ID    :", student[0])
        print("Name  :", student[1])
        print("Age   :", student[2])
        print("Marks :", student[3])
        print("Grade :", student[4])

    else:
        print("Student not found.")


# Update Student
def update_student():
    update_name = input("Enter student name to update: ")

    cursor.execute(
        "SELECT * FROM students WHERE LOWER(name) = LOWER(?)",
        (update_name,)
    )

    student = cursor.fetchone()

    if student:

        print("\nCurrent Details")
        print("---------------------------")
        print("ID    :", student[0])
        print("Name  :", student[1])
        print("Age   :", student[2])
        print("Marks :", student[3])
        print("Grade :", student[4])

        new_age = int(input("Enter New Age: "))
        new_marks = int(input("Enter New Marks: "))

        new_grade = calculate_grade(new_marks)

        cursor.execute(
            """
            UPDATE students
            SET age = ?, marks = ?, grade = ?
            WHERE LOWER(name) = LOWER(?)
            """,
            (new_age, new_marks, new_grade, update_name)
        )

        conn.commit()

        print("Student updated successfully!")

    else:
        print("Student not found.")


# Delete Student
def delete_student():
    delete_name = input("Enter student name to delete: ")

    cursor.execute(
        "DELETE FROM students WHERE LOWER(name) = LOWER(?)",
        (delete_name,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


# Show Menu
def show_menu():
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# Main Function
def main():

    create_table()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Program Closed")
            conn.close()
            break

        else:
            print("Invalid Choice")


# Program Start
main()