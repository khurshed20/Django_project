#from django.contrib import admin
from django.urls import path
from . import views  # (.) means this directory location

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('stu/',views.student_info),
    path('add',views.add)

]