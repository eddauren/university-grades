from django.core.management.base import BaseCommand
from db import get_connection
from academics.models import Course, Student, Enrollment

class Command(BaseCommand):
    help="Import data feom the legacy university_grades database"

    def handle(self,*args,**options):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, code FROM courses ORDER BY id")
                courses= cur.fetchall()
                cur.execute("SELECT id, name, email, birth_date FROM students ORDER BY id")
                students=cur.fetchall()
                cur.execute("SELECT id, student_id, course_id, grade FROM enrollments ORDER BY id")
                enrollments=cur.fetchall()
        for row in courses:
            Course.objects.update_or_create(
                id=row["id"],
                defaults={"name": row["name"], "code": row["code"]},
            )
        for row in students:
            Student.objects.update_or_create(
                id=row["id"],
                defaults={"name":row["name"], "email": row["email"], "birth_date":row["birth_date"]},
            )

            for row in enrollments:
                Enrollment.objects.update_or_create(
                    id=row["id"],
                    defaults={
                        "student_id": row["student_id"],
                        "course_id": row["course_id"],
                        "grade": row["grade"]
                    },
                )
        self.stdout.write(f"Imported {len(courses)} courses")
        self.stdout.write(f"Imported {len(students)} students")
        self.stdout.write(f"Imported {len(enrollments)} enrollments")
