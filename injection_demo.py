from db import get_connection
def find_student_safe(conn,name):
    query="SELECT id, name, email FROM students WHERE name = %s"
    with conn.cursor() as cur:
        cur.execute(query, (name,))
        return cur.fetchall()
def find_student_unsafe(conn,name):
    query=f"SELECT id, name, email FROM students WHERE name = '{name}'"
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
with get_connection() as conn:
    print(find_student_unsafe(conn, "Aigerim Nurlanova"))
    print(find_student_unsafe(conn, "Aigerim Nurlanova' OR '1'='1"))
    print(find_student_safe(conn, "Aigerim Nurlanova"))
    print(find_student_safe(conn, "Aigerim Nurlanova' OR '1'='1"))