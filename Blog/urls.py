from django.urls import path
from .views import creatBlog

urlpatterns = [
    path("create-post/", creatBlog),
]
