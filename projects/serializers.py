from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'project_name', 'is_owner'
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
