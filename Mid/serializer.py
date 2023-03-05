from rest_framework import serializers
from .models import TaskList


class TaskListSerializer(serializers.ModelSerializer):
    """ Class serializer task. """
    user_name = serializers.CharField(source='get_username', read_only=True)

    class Meta:
        model = TaskList
        fields = ['id', 'task', 'insert_by', 'user_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
