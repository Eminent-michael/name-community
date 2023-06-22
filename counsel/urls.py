from django.urls import path
from .views import createCounselRoom, counselListPage, counselRoom


urlpatterns = [
    path("", counselListPage, name="counsel-listing"),
    path("room/<int:pk>/<slug:slug>", counselRoom, name="counsel-room"),
    path('create-room', createCounselRoom, name="createRoom")
]
