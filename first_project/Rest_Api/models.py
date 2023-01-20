from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    #company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    mail=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=25)
    about=models.TextField(max_length=1000,choices=(("IT","IT"),("Non IT","Non IT"),("mobile","mobile")))
    
    def __str__(self):
        return self.name+ " , "+ self.mail


class Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Topic_Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.CharField(max_length=500)
    date_added=models.DateTimeField(auto_now_add=True)
    
     
    class Meta:
        verbose_name_plural='topic_entry'
        
        def __str__(self):
          return f"{self.text[:30]}.."        
          
class Topic_Entry_comment(models.Model):
     topic_entry=models.ForeignKey(Topic_Entry,on_delete=models.CASCADE)
     text=models.CharField(max_length=500)
     date_added=models.DateTimeField(auto_now_add=True)
     commenter=models.ForeignKey(User,on_delete=models.CASCADE)
         
    
     class Meta:
        verbose_name_plural='topic_entry_comment'
       
        def __str__(self):
          return f"{self.text[:30]}.." 