from .serializers import userSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

class userviewsets(viewsets.ModelViewSet):

    #authentication_classes=[TokenAuthentication]
    authentication_classes=[TokenObtainPairView]
    permission_classes=[IsAuthenticated]  
   
    queryset= User.objects.all()
    serializer_class = userSerializer
    

   
    #def get (self, request):
       # content={ 'message': 'Hellow API Endpoint'}
       #
       # 
       #  return Response(content)