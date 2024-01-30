from django.contrib import admin
from .models import Student

# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['id','Fname','Lname','Age','Quali','Dob','Lang']