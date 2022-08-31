from django.urls import path

from api.review.views import ReviewComment

urlpatterns = [
    path("<int:pk>/comment/", ReviewComment.as_view()),
]
