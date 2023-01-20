from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def machine(request):
    course="machine learning"
    clas = 21
    seat = 20
    duration = "2.5 Months"
    no =[2,3,4,5,8,70]
    dict={'key1':20,'key2':30,'key3':40,'key4':50,'key5':60}
    offering={'c':course,'tc':clas,'st':seat,'cd':duration, 'dict':dict, 'no':no}
    
    #return HttpResponse ("WElcome to Django: My first Django project with Python")
    return render (request, 'machine-learning/machine-learning1.html',context=offering)
@login_required    
def machine_01(request):
    #return HttpResponse("this view output through 'from machine_learing import views as v' url method")
    return render (request, 'machine-learning/machine-learning2.html')
    
@login_required    
def machine_02(request):
    #return HttpResponse("this view output through 'from machine_learing.views import machine_02' url method"")
    return render (request, 'machine-learning/machine-learning3.html')