from db import get_connection
from pathlib import Path
BASE_DIR=Path(__file__).parent
QUERY_PATH=BASE_DIR / 'queries' / 'top_student_per_course.sql'

def get_top_students(conn):
    query=QUERY_PATH.read_text(encoding='utf-8')
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def main():
    with get_connection() as conn:
        rows=get_top_students(conn)
        print(f"|{'Course':<22}|{'Student':<22}|{'Grade':>5}|")
        print("-"*53)
        for _,student,course,grade in rows:
            grade_text=grade if grade is not None else "-"
            print(f"|{course:<22}|{student:<22}|{grade_text:>5}|")
            print("-"*53)


if __name__ =="__main__":
    main()