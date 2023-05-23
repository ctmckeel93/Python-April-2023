from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index),
    path('home', views.home),
    path("home/<name>", views.hello),
    path("process", views.process),
    path("display", views.display)
]