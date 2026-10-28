from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import functions

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=10 , unique=True)

    def __str__(self):
        return self.code
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    birth_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.CheckConstraint(
                condition=models.Q(birth_date__lt=functions.TruncDate(functions.Now())),
                name="birth_date_in_past"
            )
        ]

    def __str__(self):
        return self.name
class Enrollment(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.PROTECT)
    grade=models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0),MaxValueValidator(100)])

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['student','course'], name='unique_student_course'),
            models.CheckConstraint(condition=models.Q(grade__gte=0, grade__lte=100),name="grade_between_0_and_100",)
        ]
