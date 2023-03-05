from rest_framework import routers

from .views import TasklistViewSet

task_patterns = routers.DefaultRouter()
task_patterns.register(r'', TasklistViewSet, basename='Task')
