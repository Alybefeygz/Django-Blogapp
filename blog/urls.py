from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name = "blogs_by_category"),
    path("blogs/<slug:slug>", views.blogs_details, name="blogs_details")
]