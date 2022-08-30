from rest_framework import generics

from app.review.models import Review

from api.review.serializers import ReviewDetailSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
