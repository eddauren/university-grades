from rest_framework import serializers
from .models import Student, Enrollment, Course
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= ["id", "name", "email", "birth_date"]

    def validate_birth_date(self, value):
        if value >= date.today():
            raise serializers.ValidationError("Birth date must be in the past.")
        return value
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollment
        fields=["id","student", "course", "grade"]

class SetGradeSerializer(serializers.Serializer):
    student= serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    course= serializers.PrimaryKeyRelatedField(queryset= Course.objects.all())
    grade=serializers.IntegerField(min_value=0, max_value=100)