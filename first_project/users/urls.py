
from django.urls import path, include
from . import views  # (.) means this directory location
from . views import Change_Password, Logoutuser ,Loginuser, activate, UserProfileCreate, UserProfileView
from django.contrib.auth.views import PasswordResetView , PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#app_name='users'
urlpatterns=[

    path('', include ('django.contrib.auth.urls'), name='users'),
  #  path('log_out/',views.log_out, name='log_out'),
    #path('register/',views.register, name='register'),
    path('location/',views.Location_Api.as_view(), name='Location_Api'),
    path('api_test/',views.userApiView.as_view()), 
    path('signup/',views.registration, name='signup'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('password/',Change_Password, name='password'),
    path('log_out/',Logoutuser, name='logout'),
    path('log_in/',Loginuser, name='login'),
    path('user_profile_create/',UserProfileCreate, name='UserProfileCreate'), 
    path('user_profile/',UserProfileView, name='UserProfileView'),

    
    path('reset/password/',PasswordResetView.as_view(template_name='registration/reset_pass.html'), name='password_reset'),
    path('password/reset/done/',PasswordResetDoneView.as_view(template_name='registration/reset_pass_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # soicial login ,logout 
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),

]  