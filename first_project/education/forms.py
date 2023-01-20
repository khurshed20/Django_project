from django import forms
from .models import  RecordModel , PostModel

class RecordForm(forms.ModelForm):
    name = forms.CharField(initial='Your name', label='Your Name')
    email=forms.EmailField(initial="your Email Id")
    label={'amount':'Your Amount'}
    class Meta:
        model=RecordModel
        exclude=['user','slug','created_at']
        widgets={
            'SubjectModel':forms.CheckboxSelectMultiple(attrs={'multiple':True,}),
             'GroupModel':forms.CheckboxSelectMultiple(attrs={'multiple':True,}),
            
        }
        labels={ 'subject': 'Your Subjects : ', 'group':'Your Group', 'medium':'Select Medium'

    }
    #def __init__ (self, *args, **kwargs):
       # super(). __init__(*args, **kwargs)
       # self.fields['name'].label="Your Name"
        #self.fields['address'].initial='My Present Address : '
    
   
class PostForm(forms.ModelForm):
    
    class Meta:
        model =PostModel
        exclude=['user','created_at']

   