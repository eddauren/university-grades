
import psycopg
from db import get_connection
from grades import set_grade
from top_students import get_top_students

def ask_set_grade(conn):
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = int(input("Enter grade (0-100): "))
    print(set_grade(conn, student_id, course_id, grade))
    conn.commit()


def main():
    with get_connection() as conn:
        while True:
            print("\n1. Set grade")
            print("2. Show top students")
            print("0. Exit")
            choice = input("Choice: ")
            if choice == "1":
                try:
                    ask_set_grade(conn)
                except ValueError:
                    print("Invalid input. Please enter valid integers.")
                except psycopg.errors.CheckViolation:
                    print('grade must be between 0 and 100.')
                    conn.rollback()
                except psycopg.errors.ForeignKeyViolation:
                    print('Student or Course does not exist.')
                    conn.rollback()
            elif choice == "2":
                rows = get_top_students(conn)
                for _, student, course, grade in rows:
                    grade_text = grade if grade is not None else "-"
                    print(course, student, grade_text)
            elif choice == "0":
                break
            else:
                print("Unknown option")

if __name__ == "__main__":
    main()