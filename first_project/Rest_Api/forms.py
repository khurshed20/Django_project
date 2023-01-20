from django import forms 
from . models import Topic, Topic_Entry , Company
from . import models
from captcha.fields import CaptchaField
class TopicForm (forms.ModelForm):

    captcha=CaptchaField()
    class Meta:
        model =Topic
        fields=['text']
        labels={'text':'Topic'}

class EntryForm(forms.ModelForm):
     class Meta:
        model= models.Topic_Entry
        #model=Topic
        fields=['text']
        labels={'text':'Enter Topic Details '}
        wigets={'text':forms.Textarea(attrs={'cols':80})}

class EntryCommentForm(forms.ModelForm):
     class Meta:
        model= models.Topic_Entry_comment
        #model=Topic
        fields=['text']
        labels={'text':'Enter comment '}
        wigets={'text':forms.Textarea(attrs={'cols':80})}

class CompanyModelForm(forms.ModelForm):
    
    username=forms.CharField(max_length=50 ,initial='Enter username for Authentication')
    password=forms.CharField(max_length=20, initial='Enter password for Authentication')
    class Meta :
           model=Company
           fields = '__all__'

