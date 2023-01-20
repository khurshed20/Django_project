from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField
from django.utils.timezone import datetime


# Create your models here.

class UserProfileModel(models.Model):
    Gender_choice=(('Male','Male'),('Female','Female'))
    Category_choice=(('Student','Student'),('Teacher','Teacher'))
    group_choice=(('Science','Science'),('Arts','Arts'),('Business Studies','Business Studies'))
    subject_choices_science=(('Math','Math'),('Physics','Physics'),('Chemistry','Chemistry'),('Applied Physics','Applied Physics'),('ICT','ICT'),('Applied Math','Applied Math'))
    subject_choices_arts=(('Bangla','Bangla'),('English','English'),('BGS','BGS'))
    subject_choices_Business=(('Finance','Finance'),('Accounting','Accounting'),('Economics','Economics'))

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField()
    gender=models.CharField(max_length=100,choices=Gender_choice) # single select field
    profession=models.CharField(max_length=100,choices=Category_choice)  # single select field
    group=models.CharField(max_length=100,choices=group_choice) # single select field
    
    subject_science=MultiSelectField(blank=True,max_length=200,max_choices=3,choices=subject_choices_science)
   
    subject_arts=MultiSelectField(blank=True,max_length=200,max_choices=3,choices=subject_choices_arts)
    
    subject_business=MultiSelectField(blank=True,max_length=200,max_choices=3,choices=subject_choices_Business) 

    #subjects=MultiSelectField(max_length=200,max_choices=3,choices=subject_choices_Business )
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    biodata=models.TextField()
    image=models.ImageField(upload_to= '') #'users/images')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img=Image.open(self.image.path)  
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size) 
            img.save(self.image.path) 