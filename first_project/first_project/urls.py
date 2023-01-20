"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from machine_learning import views # url method 1
from machine_learning import views as v # url method 2
from machine_learning.views import machine_02 # url method 3
from django.urls import path, include
from . router import router
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views
 # for image file upload
from django.conf import settings 
from django.conf.urls.static import static 
from django.views.generic import TemplateView
from education.views import templateview

 # image file end

urlpatterns = [
      # REST API for users
    path('user_api/',include(router.urls)),  # ultimate url => user_api/user
    path('token/',views.obtain_auth_token, name='api_token_auth'),  # this auth url also define in 'rest_api/urls.py'
    path('jwt_token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token
    # REST API for users End  
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('education/',include('education.urls')),
    path('',TemplateView.as_view(template_name='machine-learning/machine-learning1.html')),
    path('template/',templateview.as_view()),
       
    #path('',v.machine),
    path('mc1/',v.machine_01),
    path('mc2/',machine_02),
    path('data/',include('data_analysis.urls')),
    path('home1/',include('home_page.urls')),
    path('api_git/',include('api_response.urls')),
    path('rest_api/',include('rest_framework.urls')),
    path('api/', include('Rest_Api.urls')),
    path('mail/', include('mail_app.urls')),
    path('new_api/',include('New_Api.urls')),
    path('captcha', include('captcha.urls')),
    path('inbox/notifications/',include('notifications.urls',namespace='notifications')),
    path('oauth/', include('social_django.urls', namespace='social')),  

]  

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)