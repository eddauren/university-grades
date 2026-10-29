from django.shortcuts import render
from .models import Student , Enrollment
from .serializers import StudentSerializer, EnrollmentSerializer, SetGradeSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset= Enrollment.objects.all()
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