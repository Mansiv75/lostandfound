from django.contrib.auth.models import User
from rest_framework import serializers
from .models import LostItem, FoundItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=LostItem
        fields = '__all__'

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoundItem
        fields = '__all__'