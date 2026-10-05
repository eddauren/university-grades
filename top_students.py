from db import get_connection
def get_top_students(conn):
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
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def main():    
    with get_connection() as conn:
        rows=get_top_students(conn)
        print(f"|{'Course':<22}|{'Student':<22}|{'Grade':>5}|")
        print("-"*53)
        for _,student,course,grade_text in rows:
            grade_text=grade_text if grade_text is not None else "-"
            print(f"|{course:<22}|{student:<22}|{grade_text:>5}|")
            print("-"*53)
if __name__ =="__main__":
    main()