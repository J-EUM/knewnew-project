from rest_framework import generics

from app.review.models import Comment

from api.review.serializers import ReviewCommentSerializer


class ReviewComment(generics.ListAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(review_id=self.kwargs["pk"], parent_comment__isnull=True)
        print(queryset)
        return queryset

    serializer_class = ReviewCommentSerializer
