from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfileModel 

class SignUpForm(UserCreationForm):

    class Meta :
        model=User
        fields={'first_name','last_name','username','email'}

class UserProfileForm(forms.ModelForm):

    birth_date=forms.DateField(initial="YYYY-MM-DD" )
    #birth_date=forms.DateField(widget=forms.TextInput())
    class Meta:
        model =UserProfileModel  
        #fields='__all__'
        exclude =['user',] 
        #exclude=('user',) 

       
