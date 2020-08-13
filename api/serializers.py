from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']


class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        fields = ['name', 'birthdate', 'job_role']
