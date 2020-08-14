from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'user_id', 'navers']


class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        fields = ['name', 'birthdate', 'job_role', 'navers', 'user_id']
