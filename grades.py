import psycopg
from db import get_connection
def set_grade(conn,student_id,course_id,grade):
    query="""
        INSERT INTO enrollments (student_id,course_id,grade)
        VALUES (%s,%s,%s)
        ON CONFLICT (student_id,course_id) DO UPDATE
        SET grade=EXCLUDED.grade
        RETURNING id,grade
    """
    with conn.cursor() as cur:
        cur.execute(query,(student_id,course_id,grade))
        return cur.fetchone()
if __name__=="__main__":
    try:
        with get_connection() as conn:
            print(set_grade(conn, 1, 1, 92))
    except psycopg.errors.CheckViolation:
        print('grade must be between 0 and 100.')