from db import get_connection
from grades import set_grade
import psycopg

def ask_set_grade():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = int(input("Enter grade (0-100): "))
    with get_connection() as conn:
        print(set_grade(conn, student_id, course_id, grade))
if __name__ == "__main__":
    try:
        ask_set_grade()
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except psycopg.errors.CheckViolation:
        print('grade must be between 0 and 100.')
    except psycopg.errors.ForeignKeyViolation:
        print('Student or Course does not exist.')
