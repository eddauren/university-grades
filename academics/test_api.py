import pytest
from rest_framework.test import APIClient
from academics.models import Student, Course, Enrollment
from django.contrib.auth.models import User
from rest_framework.settings import api_settings

@pytest.fixture
def user():
    return User.objects.create_user(username="student", password="pass12345",is_staff=False)

@pytest.fixture
def teacher():
    return User.objects.create_user(username="teacher", password="pass12345", is_staff=True)

@pytest.fixture
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def auth_teacher(teacher):
    client=APIClient()
    client.force_authenticate(user=teacher)
    return client

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
def test_set_grade_creates_enrollment(auth_teacher,student,course):
    response = auth_teacher.put(
        "/api/set-grade/",
        {"student": student.id, "course": course.id, "grade":90},
        format="json",
    )
    assert response.status_code == 201
    assert Enrollment.objects.count()==1

@pytest.mark.django_db
def test_set_grade_updates_existing_enrollment(auth_teacher,student,course):
    response=auth_teacher.put(
        "/api/set-grade/",
        {"student":student.id, "course" : course.id, "grade":70},
        format="json"
    )
    assert response.status_code==201
    response=auth_teacher.put(
        "/api/set-grade/",
        {"student":student.id, "course" : course.id, "grade":90},
        format="json"
    )
    assert response.status_code==200
    assert Enrollment.objects.count()==1
    assert Enrollment.objects.get(student=student, course=course).grade==90

@pytest.mark.django_db
def test_set_grade_wrong_grade(auth_teacher,student,course):
    response= auth_teacher.put(
        "/api/set-grade/",
        {"student": student.id, "course":course.id, "grade":150},
        format="json"
    )
    assert response.status_code==400
    assert Enrollment.objects.count()==0

@pytest.mark.django_db
def test_set_grade_non_existing_student(auth_teacher,course):
    response= auth_teacher.put(
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
    assert row["student"]=="Test1"
    assert row["course"]=="Math"
    assert row["grade"]==100

@pytest.mark.django_db
def test_top_students_two_same_grades(client,course):
    student1=Student.objects.create(name="AAA", email="test1@example.com", birth_date="2001-01-01")
    student2=Student.objects.create(name="BBB", email="test2@example.com", birth_date="2001-01-01")
    Enrollment.objects.create(student=student1,course=course,grade=100)
    Enrollment.objects.create(student=student2,course=course,grade=100)
    response=client.get(
        "/api/top-students/"
    )
    assert response.status_code==200
    assert len(response.data)==1
    row= response.data[0]
    assert row["student"]=="AAA"
    assert row["course"]=="Math"
    assert row["grade"]==100

@pytest.mark.django_db
def test_set_grade_without_token(client,student,course):
    response=client.put(
        "/api/set-grade/",
        {"student":student.id,"course":course.id,"grade":90},
        format="json"
    )
    assert response.status_code==401
    assert Enrollment.objects.count()==0

@pytest.mark.django_db
def test_set_grade_non_staff_creates_enrollment(auth_client,student,course):
    response = auth_client.put(
        "/api/set-grade/",
        {"student": student.id, "course": course.id, "grade":90},
        format="json",
    )
    assert response.status_code == 403
    assert Enrollment.objects.count()==0

@pytest.mark.django_db
def test_students_list_is_paginated(client):
    page_size=api_settings.PAGE_SIZE
    total=page_size+1
    for i in range(total):
        Student.objects.create(
            name=f"S{i}",
            email=f"s{i}@example.com",
            birth_date="2001-01-01",
        )
    first= client.get("/api/students/")
    assert first.status_code==200
    assert first.data["count"]==total
    assert len(first.data["results"])==page_size
    assert first.data["next"] is not None
    assert first.data["previous"] is None

    second=client.get("/api/students/?page=2")
    assert second.status_code==200
    assert len(second.data["results"])==1
    assert second.data["next"] is None

    third=client.get("api/students/?page=3")
    assert third.status_code==404
