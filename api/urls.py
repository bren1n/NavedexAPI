from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('user/register', UserCreate.as_view()),
    path('user/token', jwt_views.TokenObtainPairView.as_view()),
    path('user/token/refresh', jwt_views.TokenRefreshView.as_view()),
    path('project', project_list),
    path('project/<int:id>', project_id),
    path('naver', naver_list),
    path('naver/<int:id>', naver_id)
]
