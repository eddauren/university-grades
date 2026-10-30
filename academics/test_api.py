import pytest
from rest_framework.test import APIClient
from academics.models import Student, Course, Enrollment

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    return Student.objects.create(name="Test", email="test@example", birth_date="2000-01-01")

@pytest.fixture
def course():
    return Course.objects.create(name="Math", code="M1")

@pytest.mark.django_db
def test_set_grade_creates_enrollment(client,student,course):
    response = client.put(
        "/api/set-grade/",
        {"student": student.id, "course": course.id, "grade":90},
        format="json",
    )
    assert response.status_code == 201
    assert Enrollment.objects.count()==1

@pytest.mark.django_db
def test_set_grade_updates_existing_enrollment(client,student,course):
    response=client.put(
        "/api/set-grade/",
        {"student":student.id, "course" : course.id, "grade":70},
        format="json"
    )
    assert response.status_code==201
    response=client.put(
        "/api/set-grade/",
        {"student":student.id, "course" : course.id, "grade":90},
        format="json"
    )
    assert response.status_code==200
    assert Enrollment.objects.count()==1
    assert Enrollment.objects.get(student=student, course=course).grade==90

@pytest.mark.django_db
def test_set_grade_wrong_grade(client,student,course):
    response= client.put(
        "/api/set-grade/",
        {"student": student.id, "course":course.id, "grade":150},
        format="json"
    )
    assert response.status_code==400
    assert Enrollment.objects.count()==0

@pytest.mark.django_db
def test_set_grade_non_existing_student(client,course):
    response= client.put(
        "/api/set-grade/",
        {"student": 9999, "course":course.id, "grade":100},
        format="json"
    )
    assert response.status_code==400
    assert Enrollment.objects.count()==0

@pytest.mark.django_db
def test_top_students_get(client,course):
    student1=Student.objects.create(name="Test1", email="test1@example.com", birth_date="2001-01-01")
    student2=Student.objects.create(name="Test2", email="test2@example.com", birth_date="2001-01-01")
    Enrollment.objects.create(student=student1,course=course,grade=100)
    Enrollment.objects.create(student=student2,course=course,grade=99)
    response=client.get(
        "/api/top-students/"
    )
    assert response.status_code==200
    assert len(response.data)==1
    row= response.data[0]
    assert row["student"]=="Test"
    assert row["course"]=="Math"
    assert row["grade"]==100

    