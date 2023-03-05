from rest_framework import routers

from .views import ProfileImageslistViewSet

profile_images_patterns = routers.DefaultRouter()
profile_images_patterns.register(r'profile_images', ProfileImageslistViewSet, basename='Task')
