from django.http import HttpResponse
from django.shortcuts import render
from home_page.models import Student

# Create your views here.

def home(request):
    return render(request ,'home.html') 

def student_info(request):
    stud=Student.objects.all()
    return render (request, 'home.html', {'stu':stud})

def add(request):
     if request.method =="POST" :
        val1=int(request.POST['num1'])
        val2=int(request.POST['num2'])

        val=val1+val2
     
        return render (request, 'home.html', {'result':val}  )
        