from django.shortcuts import render     # redirect() ,get_object_or_404(), get_list_or_404() , 
from rest_framework.response  import Response
import re
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
#from django.core.exceptions import ValidationError


# Create your views here.

# Create API Registration 
@api_view(['GET','POST','PATCH'])
@permission_classes([AllowAny])
def Api_Registration(request):
    print ( 'Received Ok')
   # return JsonResponse({"result":"OK"})
   # return Response({"result":"OK"})
    if request.method=="POST":
       
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        username=request.data['username']
        email=request.data['email']
        password=request.data['password']
        repassword=request.data['repassword']
        print("USERNAME:",username)
        #return Response ({"ERROR":"Invalid Email Id"})
        error=''
        error1=0
        if  password == repassword :
            if not re.findall('\d', password) or not re.findall('[A-Z]', password) or not re.findall('[a-z]', password) or not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password) :
              # return Response ({"ERROR1":"The password must contain lower-upper case, numeric and symbol "})
               error=error+"The password must contain Upper-lower case, numeric and symbol ** "
               error1=error1+1
        else :
            #return Response ({"ERROR":"Password is not matching"})
            error=error+"Password is not matching **"
            error1=error1+1  

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

       
        if not re.fullmatch(regex, email):
            #return Response ({"ERROR":"Invalid Email Id"})
            error=error+"Invalid Email Id **"
            error1=error1+1


        if not re.findall('\d', username)  or not re.findall('[a-z]', username):
             #return Response ({"ERROR":"Username should be alfha-numeric"})
             error=error+"Username should be alfha-numeric **"
             error1=error1+1
        if first_name=='' :
             error=error+"Atleast First Name is required **"
             error1=error1+1     
        if error1 :
            return Response ({"result":error})   

        if User.objects.filter(username=username).exists():
            return Response({"result":"username already existing"})
        if User.objects.filter(email=email).exists():
            return Response ({"result":"Email already used for registration"})    
        user=User()
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email
        user.is_active=True
        user.set_password(raw_password=password)
        user.save()
        data={"Name":first_name+ " "+last_name,"Username":username,"Email":email}    
        return Response({"result":"Registration Ok", "data":data})
    else :
        return Response ({"result":"Only 'POST' Method Allowed"})          
             