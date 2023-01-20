import email
from django import forms
from django.core import validators



class student_registration(forms.Form):
    first_name=forms.CharField(label='Enter Your First Name',label_suffix='*') # label='Enter Your First Name',label_suffix='*')
    last_name=forms.CharField(initial='Enter Last Name') #initial='Enter Last Name')
    email=forms.EmailField(initial='mail@khurshed.xyz',disabled=True) #initial='mail.khurshed.xyz',disabled=True)
    password=forms.CharField(widget=forms.PasswordInput) #(widget=forms.PasswordInput)
    Repassword=forms.CharField(widget=forms.PasswordInput) #(widget=forms.PasswordInput)
   
    clas=forms.CharField()
    roll=forms.IntegerField()
    text=forms.CharField(widget=forms.Textarea) #widget=forms.Textarea)
    checkbox=forms.CharField(widget=forms.CheckboxInput) #(widget=forms.CheckboxSelectMultiple)
   
    file=forms.FileField() #widget=forms.FileField)

    def clean(self):
        cleaned_data=super().clean()
        rightpassword=self.cleaned_data['password']
        repassword=self.cleaned_data['Repassword']
        if rightpassword != repassword :
            raise forms.ValidationError('Password did not match')

class fileUploadForm(forms.Form):
    file_name=forms.CharField(label="Enter File Name")
    #=forms.FileField()
    #owner=forms.CharField()
    file=forms.FileField(widget=forms.FileInput(attrs={'multiple': True})) #widget=forms.FileField)



    
