from django.urls import path

from api.review.views import CommentCreate

urlpatterns = [
    path("<int:pk>/comment/", CommentCreate.as_view()),
]
