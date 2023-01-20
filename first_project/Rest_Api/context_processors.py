from .models  import Topic
#from users.views import Location_Api 

def topicComment(request):
    TOPIC=Topic.objects.order_by('date_added')
   # ip= Location_Api() 
    #ip=ip.get(request)
    return   {'TOPIC': TOPIC }

