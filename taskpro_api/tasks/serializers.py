from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    is_owner = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'task_name', 'description', 'assignees', 'project', 'status', 'attachment', 'is_owner'
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
 

