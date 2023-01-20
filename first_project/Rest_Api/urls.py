from django.urls import path, include
from . import views  # (.) means this directory location
from Rest_Api.views import CompanyViewSets
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import company , CompanyInfo_RestApi_get # here company is class 

router=routers.DefaultRouter()
router.register('company',CompanyViewSets)
#app_name='Rest_Api'
urlpatterns = [
    #path('admin/', admin.site.urls),
   
    path('rapi/',views.firstApi),
    path('rcall/',views.rest_call),
      # REST API
    path('company/',company.as_view(), name='company'), ## class based view for REST Api
    path('company/<int:id>/',company.as_view()),    ## class based view for a particular id of REST Api
    path('api-token-auth/',obtain_auth_token, name='api_token_auth'), # this auth url also define in 'first_project/urls.py'
    # REST API End
    path('',include(router.urls)),
    path('topic/',views.topic,name='topics'),
    path('topic/<int:topic_id>/',views.entry,name='entries'),
    path('new_topic/',views.new_topic,name='new_topics'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entries'),
    path('comment/<int:entry_id>/<int:topic_id>/',views.comment_entry,name='comment_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
    path('company_apiPost/',views.CompanyInfo_RestApi_post,name='Company_RestApi_post'),
    path('company_apiGet/',views.CompanyInfo_RestApi_get,name='Company_RestApi_get'),



]
