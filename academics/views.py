from django.shortcuts import render
from .models import Student , Enrollment
from .serializers import StudentSerializer, EnrollmentSerializer, SetGradeSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from pathlib import Path

BASE_DIR=Path(__file__).parent
QUERY_PATH=BASE_DIR / "sql" / "top_students.sql"
TOP_STUDENTS_QUERY = QUERY_PATH.read_text(encoding="utf-8")

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.order_by("id")
    serializer_class=StudentSerializer
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset= Enrollment.objects.order_by("id")
    serializer_class= EnrollmentSerializer

@api_view(["PUT"])
def set_grade(request):
    serializer=SetGradeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data= serializer.validated_data
    enrollment,created=Enrollment.objects.update_or_create(
        student=data["student"],
        course=data["course"],
        defaults={"grade": data["grade"]},
    )
    status_code=201 if created else 200
    return Response(EnrollmentSerializer(enrollment).data, status=status_code)

@api_view(["GET"])
def top_students(request):
    with connection.cursor() as cur:
        cur.execute(TOP_STUDENTS_QUERY)
        columns= [col.name for col in cur.description]
        rows=[dict(zip(columns, row)) for row in cur.fetchall()]
    return Response(rows)
