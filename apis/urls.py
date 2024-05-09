from django.urls import path

from .view import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view(), name='book_list'),
]
