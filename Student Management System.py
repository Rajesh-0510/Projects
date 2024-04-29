import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="std_mgm"
)

# Create cursor
cursor = db.cursor()

# Function to add a new student
def add_student(std_id, name, email, phone):
    sql = "INSERT INTO students (std_id, name, email, phone) VALUES (%s, %s, %s, %s)"
    val = (std_id, name, email, phone)
    cursor.execute(sql, val)
    db.commit()
    print("Student added successfully")

# Function to display all students
def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)

# Function to search for a student by name
def search_student(name):
    sql = "SELECT * FROM students WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    student = cursor.fetchone()
    if student:
        print("Student found:")
        print(student)
    else:
        print("Student not found")

# Function to delete a student by ID
def delete_student(std_id):
    # Check if the student with the given ID exists
    check_sql = "SELECT * FROM students WHERE std_id = %s"
    check_val = (std_id,)
    cursor.execute(check_sql, check_val)
    existing_student = cursor.fetchone()

    if existing_student:
        # If the student exists, proceed with deletion
        delete_sql = "DELETE FROM students WHERE std_id = %s"
        delete_val = (std_id,)
        cursor.execute(delete_sql, delete_val)
        db.commit()
        print("Student deleted successfully")
    else:
        print("Student with ID {} not found. Deletion aborted.".format(std_id))

# Main menu
def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            std_id = int(input("Enter student's ID: "))
            name = input("Enter student's name: ")
            email = input("Enter student's email: ")
            phone = input("Enter student's phone: ")
            add_student(std_id, name, email, phone)
        elif choice == '2':
            display_students()
        elif choice == '3':
            name = input("Enter student's name to search: ")
            search_student(name)
        elif choice == '4':
            std_id = int(input("Enter student's ID to delete: "))
            delete_student(std_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

# Run main menu
main_menu()

# Close connection
db.close()
