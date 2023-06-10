from django.urls import path
from .views import counselingHome


urlpatterns = [
    path('', counselingHome)
]