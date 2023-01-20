from django.http import HttpResponse
from django.shortcuts import render
from . forms import student_registration, fileUploadForm

from django.contrib.auth.forms import UserCreationForm
from django.views import View 
from Rest_Api.models import Topic
from django.contrib.auth.models import User
from .models import FileUploadModel

# Create your views here.
def data_analysis_01(request):
    return render (request, 'data_analysis/data_analysis_01.html')

def data_analysis_02(request):
    return render (request, 'data_analysis/data_analysis_02.html')

def data_analysis_03(request):
    return render (request, 'data_analysis/data_analysis_03.html')

def student_information(request):
     if request.method=='POST':
        fm=student_registration(request.POST)
        fm.order_fields(field_order=['last_name','first_name','clas','roll','email','password','Repassword','text','checkbox','file'])
        if fm.is_valid():
         print(fm)
         print('This is POST Data')
         print(fm.cleaned_data)
     else :

       fm= student_registration()
       print('This is GET Data')
       
     return render (request, 'data_analysis/forms.html',{'form':fm})

def user_registration(request):
    fcm=UserCreationForm()
    if request.method=='POST':
         fcm=UserCreationForm()
         if fcm.is_valid():
            fcm.save()
         else :
            fcm =UserCreationForm()  
          
    return render (request, 'data_analysis/user_register.html',{'form':fcm})


class view_by_class(View):

    def get(self, request):

        return render (request, 'data_analysis/view_class.html')

def fileupload(request):
    owner=request.user # SessionMiddleware & AuthenticationMiddleware should be added in MIDDLEWEAR of settings.py 
                       # To get current user
    if request.method=="POST":

        file_name=request.POST.get('file_name')  
        files=request.FILES.getlist('file') 
        fm=fileUploadForm(request.POST, request.FILES) # for single file 
        
        
        if fm.is_valid(): # for single file also
            #file_name=fm.cleaned_data['file_name']  # for single file
            #file=fm.cleaned_data['file']  # for single file
           for f in files:
              model_object=FileUploadModel(file_name=file_name,file=f,owner=owner)
              #model_object=FileUploadModel(file_name=file_name,file=file,owner=owner) # for single file
            
              model_object.save() # for single file also
                                
           context={ # for single file also 
                "User":owner, "file_name":file_name
              }
            # get all images through FileUploadModel to display and also for download 
           all_files=FileUploadModel.objects.all() # for single file also

        
           return render (request, 'fileupload.html' ,{ "User":owner, "all_files":all_files}) 
           # return HttpResponseRedirect('/thanks/') 
        else:

            fm=fileUploadForm()
            return HttpResponse ("File Uploading Failed")   

    else : 

       fm=fileUploadForm()
       return render (request, 'fileupload.html' , {"form":fm, "User":owner})    
