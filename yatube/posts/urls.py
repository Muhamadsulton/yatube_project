from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path("group/", views.group_posts, name="group_posts"),
    path("group/<slug:slug>/", views.group_posts_details, name="group_posts_datails")
]