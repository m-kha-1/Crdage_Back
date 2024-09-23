from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields='__all__'

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model=PRODUCTION
        fields='__all__'
        

        
class TaskSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Task2
        fields = '__all__'
        read_only_fields = ['id']
        
class TaskSerializer2_noId(serializers.ModelSerializer):
    producer_name = serializers.CharField(source='producerID.name', read_only=True)
    production_name = serializers.CharField(source='PRODUCTIONId.name', read_only=True)
    cgSupervisor2_name=serializers.CharField(source='supervisor2ID.name', read_only=True)
    cgArtist_name=serializers.CharField(source='cgArtist3Id.name', read_only=True)
    
    class Meta:
        model=Task2
        fields='__all__'
        read_only_fields = ['id']
        

        
               
class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producer
        fields='__all__'
        
class Producer2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Producer2
        fields='__all__'
        
class CgArtist2Serializer(serializers.ModelSerializer):
    class Meta:
        model=CgArtist3
        fields='__all__'
        
class Supervisor2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor2
        fields='__all__'
        
    
class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model=Path
        fields=['id','path']
        
