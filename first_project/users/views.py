from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate, update_session_auth_hash, logout
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, AuthenticationForm
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response  import Response
from django.contrib import messages
from . forms import SignUpForm, UserProfileForm
from django.contrib.auth.models import User
from . models import UserProfileModel
from django.http import HttpResponse
# Email send for verification 


from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
UserModel=get_user_model()
# Email Verification End

# User Location Tracking
from ipware import get_client_ip
import json, urllib

# social login 
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm

# Create your views here.

#def log_out(request):

   # return render (request, 'user/log_out.htm')

def register (request):
    if request.method != "POST":
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)   

        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect ('topics') 

    context={'form':form}
    return render (request,'registration/register.html',context)

    # Registration through  forms.py 

def registration (request):
    if request.method != "POST":
        form=SignUpForm()
    else:
        form=SignUpForm(data=request.POST)   
        #form.order_fields(field_order=['first_name','last_name','username','email'])
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            print('Email :', email)
            user=authenticate(username=username)
            print('User :', user)
            if user is not  None :
                form=SignUpForm()
                messages.error(request,'User Exists !')
                return render (request, 'registration/register.html',{'form':form})

            #user=authenticate(email=email)
            
            print('USER _email :',user)
            #if user is not None :
            if User.objects.filter(email=email).exists() :
                form=SignUpForm()
                messages.error(request,'Email already  Exists !')
                return render (request, 'registration/register.html',{'form':form})
            user=form.save(commit=False) # To make the account inactive , commit=false
            user.is_active=False # user account is made to inactive
            user.save()

            # Email send to registered user for verification 
            current_site=get_current_site(request)
            mail_subject="Activate Your Registered Account"
            message=render_to_string('registration/account.html',{
                'user':username, 'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user)
                  } )
            send_mail=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message, to=[send_mail])
            email.send()
            # Email end
            messages.success(request, 'Successfully created account')
            messages.info(request,'Activate your account through the link sent to your mail id')
            return redirect('login')
         
    context={'form':form}
    return render (request,'registration/register.html',context)


def activate(request,uidb64,token):
    try :
        uid=urlsafe_base64_decode(uidb64).decode()
        user=UserModel._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist) :
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Your Account is activated now, you can login now')
        return redirect ('login')
    else:
        messages.warning(request, 'Invalid link ,you can signup again')
        return redirect ('signup')    

def Change_Password(request):
    if request.method != "POST":
        form=PasswordChangeForm(user=request.user)
        return render (request,'registration/change_pass.html',{'form':form})  

    else:
        form=PasswordChangeForm(data=request.POST, user=request.user)   
        
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            form.save()
            messages.success(request,'Password Changed Successfully !')
            return redirect ('login') 
        else:    
            messages.success(request,'Password Change Failed ! Please Try Again')
            form=PasswordChangeForm(user=request.user)
            return render (request,'registration/change_pass.html',{'form':form})

def Loginuser(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('topics')
            else :
                messages.error(request, 'Invalid Username or Password')
                form=AuthenticationForm()
                return render (request, 'registration/login.html',{'form':form})  

        else :
            messages.error(request, 'Invalid Username or Password')
            form=AuthenticationForm()
            return render (request, 'registration/login.html',{'form':form})  
    else:
        form=AuthenticationForm()
        return render (request, 'registration/login.html',{'form':form})       


def Logoutuser(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect ('topics')


class userApiView(APIView):
    #authentication_classes=[TokenAuthentication]
    authentication_classes=[TokenObtainPairView]
    permission_classes=[IsAuthenticated]   

    def get (self, request):
        content={ 'message': 'Hellow API Endpoint'}
        return Response( content)

def UserProfileCreate(request):
    try :
        instance=UserProfileModel.objects.get(user=request.user)
    except UserProfileModel.DoesNotExist :
        instance=None
    if request.method=="POST":
       
        if instance :
           form=UserProfileForm(request.POST, request.FILES,instance=instance) 
        else:
            form=UserProfileForm(request.POST, request.FILES) 
        if form.is_valid():
            error=0         
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            s=form.cleaned_data['subject_science'] # get subject objects for iteration of multiple subject entry
            a=form.cleaned_data['subject_arts']
            b=form.cleaned_data['subject_business']
            if (len(s) and len(a) and len(b) ) or (len(s) and len(a)) or (len(b) and len(a)) or (len(b) and len(s)):  # list object
                error=1
                msg='Please Select only one Group Subject/Subjects'
           # elif len(s) and len(a) :
                #error=1
               # msg='Please Select only one Group Subject/Subjects'
            #elif len(b) and len(a) : 
               # msg='Please Select only one Group Subject/Subjects' 
               # error=1 
            #elif len(b) and len(s) : 
               # msg='Please Select only one Group Subject/Subjects' 
               # error=1     
            else :

             if len(s):
               obj.subject_science.clear()
               for i in s:
                obj.subject_science.append(i)
                obj.save()
             elif len(a): 

               #subject_arts=form.cleaned_data['subject_arts'] # get subject objects for iteration of multiple subject entry
               obj.subject_arts.clear()
               for i in a:
                  obj.subject_arts.append(i)
                  obj.save()
             elif len(b):    
               #subject_business=form.cleaned_data['subject_business'] # get subject objects for iteration of multiple subject entry
               obj.subject_business.clear()
               for i in b:
                 obj.subject_business.append(i)
                 obj.save()  
             else :
                error=1
                msg='Please Choose Group Subject'      
            if error :
               messages.error(request, msg) 
               return render (request, 'registration/user_profile_create.html', {'form':form})   
            else :
                messages.success(request, 'Successfully saved your profile') 
                return redirect ('topics')
        else :
             messages.success(request, 'Submission Failed') 
             return render (request, 'registration/user_profile_create.html', {'form':form})     
    else:
        form=UserProfileForm(instance=instance)  
        return render (request, 'registration/user_profile_create.html', {'form':form})


def UserProfileView(request):
    userprofile=UserProfileModel.objects.get(user=request.user)

    return render (request, 'registration/user_profile_view.html', {'userprofile':userprofile})

class Location_Api(APIView) :
    def get(self,request,format=None) :
        client_ip , is_routable=get_client_ip(request)  

        if client_ip is None:
            client_ip="0.0.0"
        else :
            if is_routable :
                ip_type="public"
            else :
                ip_type = "private"   
       # return HttpResponse  ('Client Type: '+ip_type + ' & ' 'Client Ip :'+client_ip)  
       # ip_address= "116.204.228.58" 
        ip_address="66.249.66.197"
        #ip_address=client_ip
        url="https://api.ipfind.com/?ip="+ip_address
        respon=urllib.request.urlopen(url)
        data1=json.loads(respon.read())
        data1['client_ip']=client_ip
        data1['ip_type']=ip_type 
        return Response (data1) 
        #return HttpResponse(data1)  

    # SOCIAL LOGIN RELATED VIEWS
    
@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None


    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'registration/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('topics')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})


