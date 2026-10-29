WITH course_avg AS (
    SELECT 
        course_id, 
        AVG(grade) AS avg_grade 
    FROM academics_enrollment
    GROUP BY course_id
), 
ranked AS (
    SELECT 
        student_id,
        course_id,
        grade,
        ROW_NUMBER() OVER (
            PARTITION BY course_id 
            ORDER BY grade, student DESC NULLS LAST
        ) AS rn 
    FROM academics_enrollment
) 
SELECT 
    s.id,
    s.name as student,
    c.name AS course,
    r.grade 
FROM ranked as r 
JOIN academics_course as c ON r.course_id=c.id 
JOIN academics_student as s ON r.student_id=s.id 
JOIN course_avg as ca ON r.course_id=ca.course_id 
WHERE r.rn=1
 AND ca.avg_grade>80
ORDER BY c.name;