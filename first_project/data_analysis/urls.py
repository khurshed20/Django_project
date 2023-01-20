#from django.contrib import admin
from django.urls import path
from . import views  # (.) means this directory location

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('da1/',views.data_analysis_01,name='data1'),
    path('da2/',views.data_analysis_02 , name='data2'),
    path('da3/',views.data_analysis_03 ,name='data3'),
    path('form/',views.student_information),
    path('user_register/',views.user_registration),
    path('class/',views.view_by_class.as_view()),
    path('upload/',views.fileupload ,name='fileupload'),

]