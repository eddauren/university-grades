import os
import psycopg
from dotenv import load_dotenv
load_dotenv()

string=(
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')} "
    f"host={os.getenv('DB_HOST')}"
)
query="""WITH course_avg AS (
    SELECT 
        course_id, 
        AVG(grade) AS avg_grade 
    FROM enrollments 
    GROUP BY course_id
), 
ranked AS (
    SELECT 
        student_id,
        course_id,
        grade,
        ROW_NUMBER() OVER (
            PARTITION BY course_id 
            ORDER BY grade DESC NULLS LAST
        ) AS rn 
    FROM enrollments
) 
SELECT 
    s.id,
    s.name as student,
    c.name AS course,
    r.grade 
FROM ranked as r 
JOIN courses as c ON r.course_id=c.id 
JOIN students as s ON r.student_id=s.id 
JOIN course_avg as ca ON r.course_id=ca.course_id 
WHERE r.rn=1
 AND ca.avg_grade>80
ORDER BY c.name;"""

with psycopg.connect(string) as conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows=cur.fetchall()
        for row in rows:
            print(row)