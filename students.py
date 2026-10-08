import psycopg
from db import get_connection
def add_student(conn,name,email,birth_date):
    query= """
        INSERT INTO students (name,email,birth_date)
        VALUES(%s,%s,%s)
        RETURNING id
    """
    with conn.cursor() as cur:
        cur.execute(query,(name,email,birth_date))
        return cur.fetchone()["id"]

if __name__=="__main__":
    try:
        with get_connection() as conn:
            new_id = add_student(conn, "Test Three", "test3@example.com", "2007-05-01")
            print("Created student id:", new_id)
    except psycopg.errors.UniqueViolation:
        print("Student with this email already exists.")