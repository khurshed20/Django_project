from django.db import models

# Create your models here.

class Student(models.Model):
   
    student_name=models.CharField(max_length=40)
    student_class=models.CharField(max_length=10)
    
    student_email=models.CharField(max_length=30)
