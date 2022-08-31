from rest_framework import generics

from app.review.models import Comment

from api.review.serializers import CommentCreateSerializer


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
