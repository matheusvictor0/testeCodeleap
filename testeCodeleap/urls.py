from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appcodeleap.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'careers', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

