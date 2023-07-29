from .models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = BlogSerializer
