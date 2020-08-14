from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
