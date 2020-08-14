from django.urls import path
from images.views import (ImageCreateAPIView, ImageRetrieveUpdateAPIView,
                          ImageURLAPIView)

urlpatterns = [
    path('', ImageCreateAPIView.as_view()),
    path('<int:pk>/', ImageRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/url/', ImageURLAPIView.as_view()),
]
