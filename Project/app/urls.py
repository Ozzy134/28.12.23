from django.urls import path
from .views import ListPosts, index, imageView

urlpatterns = [
    path('', ListPosts.as_view(), name='home'),
    path('test', index),
    path('image', imageView, name='image'),
]

