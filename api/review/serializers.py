from rest_framework import serializers

from app.review.models import Comment, Review
from app.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "nickname"]


class ReviewCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    child_comments = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "created_at", "like_count", "description", "user", "child_comments"]

    def get_child_comments(self, obj):
        child = obj.comment_set.all()
        return ReviewCommentSerializer(instance=child, many=True).data
