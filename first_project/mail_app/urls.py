from django.urls import path
from . import views  # (.) means this directory location

urlpatterns = [
    #path('admin/', admin.site.urls),
   
    path('',views.mail_send),
    

]