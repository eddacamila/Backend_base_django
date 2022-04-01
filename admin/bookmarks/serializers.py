from rest_framework import serializers
from .models import Bookmark
from django.contrib.auth.models import User

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['title', 'url' , 'status' ,'user', 'created_at']
        #extra_kwards = {'status':{ 'write_only': True}}

class BookmarkSerializer_return(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'created_at']
        #extra_kwards = {'status':{ 'write_only': True}}
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwards = {'password':{ 'write_only': True}}
        