from django.contrib import admin
from .models import Student, Course, Enrollment
# Register your models here.
# admin.site.register(Course)
# admin.site.register(Student)
# admin.site.register(Enrollment)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("name", "email", "birth_date")
    search_fields=("name", "email")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=("code","name")
    search_fields=("code","name")

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "grade")
    list_filter= ('course',)
