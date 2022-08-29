from django.urls import path

from api.review.views import ReviewDetail

urlpatterns = [
    path("<int:pk>", ReviewDetail.as_view()),
]
