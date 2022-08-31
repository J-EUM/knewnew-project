from rest_framework import serializers

# from rest_framework.serializers import HiddenField, CurrentUserDefault

from app.review.models import Comment, Review
from app.user.models import User


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["review", "user", "parent_comment", "like_count", "description"]

    review = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all(), required=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    parent_comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), required=False, allow_null=True
    )
    description = serializers.CharField(max_length=100)
