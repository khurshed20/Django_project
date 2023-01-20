from  django.urls import path
from . views import templateview, RecordView,RecordView_by_class, RecordDisplay, PostCreateView, PostListView 
from . views import search, PostDetailView ,PostEditView, PostDeleteView, filter, likepost , add_comment, notification
urlpatterns = [
    #path('admin/', admin.site.urls),
     path('record/',RecordView,name='recordview'),
     path('search/',search,name='search'),  
     path('filter/',filter,name='filter'),
    #path('record/',RecordView_by_class.as_view(),name='recordview'), ## Generic FormView by class based method
    path('record_display/',RecordDisplay,name='record_display'), 
    path('post_create/',PostCreateView.as_view(),name='PostCreateView'), # Generic CreateView
    path('post_list/',PostListView.as_view(),name='PostListView'), # Generic ListView
    path('post_details/<int:pk>/', PostDetailView.as_view(),name='PostDetailView'), # Generic DetailView <int :id >
    path('post_edit/<int:pk>/', PostEditView.as_view(),name='PostEditView'), # Generic UpdateView <int :id >
    path('post_delete/<int:pk>/', PostDeleteView.as_view(),name='PostDeleteView'), # Generic UpdateView <int :id >
    path('likepost/<int:id>',likepost,name='likepost'),
    path('add_comment/',add_comment,name='add_comment'), 
    path('notification/',notification,name='notification'), 

] 
