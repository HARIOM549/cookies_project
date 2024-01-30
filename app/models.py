from django.db import models

# Create your models here.

class Student(models.Model):
    Fname=models.CharField(max_length=200,null=True)
    Lname=models.CharField(max_length=200,null=True)
    Age=models.CharField(max_length=200,null=True)
    Dob=models.CharField(max_length=200,null=True)
    Quali=models.CharField(max_length=200,null=True)
    Lang=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Fname