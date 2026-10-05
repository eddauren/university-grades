from db import get_connection
import top_students

with get_connection() as conn:
    rows=top_students.get_top_students(conn)
    for _,student,_,_ in rows:
        print(student)