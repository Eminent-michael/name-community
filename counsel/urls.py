from django.urls import path
from .views import createCounselRoom, counselListPage, counselRoomPage


urlpatterns = [
    path("", counselListPage, name="counsel-listing"),
    path("room/<int:pk>/<slug:slug>", counselRoomPage, name="counsel-room"),
    path('create-room', createCounselRoom, name="createRoom")
]
