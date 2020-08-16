from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def project_list(request):
    if request.method == 'GET':
        queryset = Project.objects.all()
        project_name = request.query_params.get('name', None)
        if project_name is not None:
            projects = queryset.filter(user=request.user.id, name__icontains=project_name)
        else:
            projects = queryset.filter(user=request.user.id)
        serializer = ProjectSerializer(projects, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = request.user.id
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def project_id(request, id):
    try:
        project = Project.objects.get(id=id, user=request.user.id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def naver_list(request):
    if request.method == 'GET':
        queryset = Naver.objects.all()
        naver_name = request.query_params.get('name', None)
        job_role = request.query_params.get('job_role', None)
        initial_date = request.query_params.get('initial_date', None)
        final_date = request.query_params.get('final_date', None)

        if job_role is not None:
            navers = queryset.filter(user=request.user.id,
                                     job_role__icontains=job_role)
        elif naver_name is not None:
            navers = queryset.filter(user=request.user.id,
                                     name__icontains=naver_name)
        elif initial_date is not None and final_date is not None:
            navers = queryset.filter(user=request.user.id,
                                     admission_date__range=[initial_date, final_date])
        else:
            navers = queryset.filter(user=request.user.id)

        serializer = NaverSerializer(navers, context={'request': request}, many=True)


        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NaverSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['user_id'] = request.user.id
            serializer.save()

            projects = request.data['projects']

            for id_project in projects:
                project = Project.objects.get(id=id_project)
                project.navers.add(serializer.data['id'])

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def naver_id(request, id):
    try:
        naver = Naver.objects.get(id=id, user_id=request.user.id)
    except Naver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaverSerializer(naver, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'DELETE':
        naver.delete()
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = NaverSerializer(naver, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

        new_projects = request.data['projects']
        old_projects = Project.objects.filter(navers=id)

        for old_project in old_projects:
            old_project.navers.remove(id)

        for new_project in new_projects:
            project = Project.objects.get(id=new_project)
            project.navers.add(serializer.data['id'])

        return Response(serializer.data)
