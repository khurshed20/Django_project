from django.db import models

# Create your models here.
class Student01(models.Model):
   
    student_name=models.CharField(max_length=40)
    student_class=models.CharField(max_length=10)
    student_roll=models.IntegerField()
    student_email=models.CharField(max_length=30)

class FileUploadModel(models.Model):
    file_name=models.CharField(max_length=40)
    #=forms.FileField()
    owner=models.CharField(max_length=100)
    file=models.FileField(upload_to='') #widget=forms.FileField)

    def __str__(self):
        return self.file_name
     