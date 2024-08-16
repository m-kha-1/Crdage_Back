from rest_framework import serializers
# from .models import MyFiles

# class MyFilesSerializer(serializers.Serializer):
#     model=MyFiles
#     fields="__all__"
    
from .models import Stockage 
    
class StockageSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Stockage
        fields=['name','media_root','media_url']
        
        
        
