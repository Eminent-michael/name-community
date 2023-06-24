from django.urls import path

from .views import categories


urlpatterns = [
    path("<str:title>", categories, name='category')
]