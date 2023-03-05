from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import ProfileImages


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProfileImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImages
        fields = ['id', 'user', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
