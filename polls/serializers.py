from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'date', 'urlCTA', 'imgPost', 'create_at')
        read_only_fields = ('created_at',)
