from django.urls import path
from .views import createBlog, blogHomePage, blogDetail

urlpatterns = [
    path("create-post/", createBlog, name="createBlogPost"),
    path("", blogHomePage, name="blogHome"),
    path("blog-details/<int:pk>/<slug:post>", blogDetail, name="blogDetails"),
]
