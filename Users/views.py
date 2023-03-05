from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializer import ProfileImagesSerializer
from .models import ProfileImages


class ProfileImageslistViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Tasklist.
    """
    queryset = ProfileImages.objects.all().order_by('-id')
    serializer_class = ProfileImagesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user', 'created_at', 'updated_at']
    search_fields = ['user']
    ordering_fields = '__all__'
