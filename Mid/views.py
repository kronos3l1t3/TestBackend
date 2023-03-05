from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializer import TaskListSerializer
from .models import TaskList


class TasklistViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Tasklist.
    """
    queryset = TaskList.objects.all().order_by('-id')
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['task', 'insert_by']
    search_fields = ['insert_by']
    ordering_fields = '__all__'
