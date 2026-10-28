from rest_framework import serializers
from .models import Student
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= ["id", "name", "email", "birth_date"]

    def validate_birth_date(self, value):
        if value >= date.today():
            raise serializers.ValidationError("Birth date must be in the past.")
        return value