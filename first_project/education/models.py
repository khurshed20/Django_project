from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from users.models  import  UserProfileModel
from PIL import Image
from multiselectfield import MultiSelectField
from django.utils.text import slugify
# Create your models here.
class RecordManager(models.Manager):
    def sorted(self, name):
        return self.order_by(name)
        
class GroupModel(models.Model):

    name=models.CharField(max_length=20)

    def __str__ (self):
        return self.name

class SubjectModel(models.Model):

    name=models.CharField(max_length=20)

    def __str__ (self):
        return self.name

class RecordModel(models.Model):
   
    Category=(('Teacher','Teacher'),('Student','Student'))
    Medium=(('Bangla','Bangla'),('English','English'),('Spanish','Spanish'),('Hindi','Hindi'),('Arabic','Arabic'))

    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    slug=models.CharField(max_length=50, default=name)
    staff_id=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    amount=models.FloatField()
    available=models.BooleanField()
    category=models.CharField(max_length=100, choices=Category)
    medium=MultiSelectField(choices=Medium,max_choices=3,default='Bangla')
    created_at=models.DateTimeField(default=now)
    image=models.ImageField(upload_to='images')
    subject=models.ManyToManyField(SubjectModel,related_name='subject_set') 
    group=models.ManyToManyField(GroupModel,related_name='group_set')
    likes=models.ManyToManyField(User,related_name='record_likes')
    views=models.ManyToManyField(User,related_name='record_views')

    def __str__ (self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
       
        super(RecordModel,self).save(*args, **kwargs)

    def address_short(self):
        address_words=self.address.split(' ')
        if len(address_words) >10:
            return ' '.join(address_words[:10])+"....."
        else:
             return self.address 

    def get_subject_list(self):

        sub=self.subject.all()
        subjects=''
        for s in sub:
            subjects=subjects+ str(s.name)+',' 
        return subjects
        
    def lowercase(self):
        return self.name.lower() 

    def total_likes(self):
        return self.likes.count()

    def total_views(self):
        
        return self.views.count()

    objects=models.Manager()
    objects=RecordManager()
    items=RecordManager()



class PostModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    clas=models.CharField(max_length=10)
    roll=models.IntegerField()
    email=models.CharField(max_length=30)
    image=models.ImageField(upload_to='')
    description=models.TextField()
    created_at=models.DateTimeField(default=now)


    def __str__ (self):
        return self.name

class Comment (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    post=models.ForeignKey(RecordModel, on_delete=models.CASCADE)
    text=models.TextField()
    parent_comment=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(default=now)
    def __str__(self):
     #return self.user.username + " :" +self.text[0:20]
     return self.text
