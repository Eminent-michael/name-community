from django.urls import path
from .views import creatBlog, blogHomePage, blogDetail

urlpatterns = [
    path("create-post/", creatBlog, name="createBlogPost"),
    path("", blogHomePage, name="blogHome"),
    path("blog-details/<int:pk>/<slug:post>", blogDetail, name="blogDetails"),
]
