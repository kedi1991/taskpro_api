from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework import status
from taskpro_api.permissions import IsOwnerOrReadOnly

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many= True, context= {'request' : request})
        return Response(serializer.data)


class TaskDetail(APIView):

    #Simplify the API view
    serializer_class = TaskSerializer
    permission_classes =[IsOwnerOrReadOnly]


    def get_object(self, pk):
        try:
            task=Task.objects.get(pk=pk)
            self.check_object_permissions (self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer=TaskSerializer(task, context= {'request' : request})
        return Response(serializer.data)

    def put (self, request, pk):
        task =self.get_object(pk)
        serializer=TaskSerializer(task, data=request.data, context= {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




