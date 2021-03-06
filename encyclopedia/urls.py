from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("edit", views.edit, name="edit"),
    path("new", views.new, name="new"),
    path("<str:title>", views.getpage, name="getpage")
    
]
