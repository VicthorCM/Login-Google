from django.urls import path
from .views import *
urlpatterns = [
    path("",home),
    path("profile/",profile,name="profile"),
]