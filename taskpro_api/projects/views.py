from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.http import Http404
from rest_framework import status
from taskpro_api.permissions import IsOwnerOrReadOnly

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many= True, context= {'request' : request})
        return Response(serializer.data)


class ProjectDetail(APIView):

    #Simplify the API view
    serializer_class = ProjectSerializer
    permission_classes =[IsOwnerOrReadOnly]


    def get_object(self, pk):
        try:
            project=Project.objects.get(pk=pk)
            self.check_object_permissions (self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer=ProjectSerializer(project, context= {'request' : request})
        return Response(serializer.data)

    def put (self, request, pk):
        project =self.get_object(pk)
        serializer=ProjectSerializer(project, data=request.data, context= {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




