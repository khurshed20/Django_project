from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):

    name=serializers.CharField(max_length=30 , required=True)
    address=serializers.CharField(max_length=200 , required=True)
    mail=serializers.EmailField(max_length=50,required=True)
    mobile=serializers.CharField(max_length=20,required=True)
    about=serializers.CharField(max_length=1000,required=True)

    class Meta:
        model= Company
        fields=('__all__')



    


