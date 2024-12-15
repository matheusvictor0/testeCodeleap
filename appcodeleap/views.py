from rest_framework import viewsets
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
