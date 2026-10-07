
import psycopg
from db import get_connection
from grades import set_grade
from top_students import get_top_students

def ask_set_grade():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = int(input("Enter grade (0-100): "))
    with get_connection() as conn:
        print(set_grade(conn, student_id, course_id, grade))
def main():
    while True:
        print("\n1. Set grade")
        print("2. Show top students")
        print("0. Exit")
        choice = input("Choice: ")
        if choice == "1":
            try:
                ask_set_grade()
            except ValueError:
                print("Invalid input. Please enter valid integers.")
            except psycopg.errors.CheckViolation:
                print('grade must be between 0 and 100.')
            except psycopg.errors.ForeignKeyViolation:
                print('Student or Course does not exist.')
        elif choice == "2":
            with get_connection() as conn:
                rows = get_top_students(conn)
                for _, student, course, grade in rows:
                    print(course, student, grade)
        elif choice == "0":
            break
        else:
            print("Unknown option")

if __name__ == "__main__":
    main()