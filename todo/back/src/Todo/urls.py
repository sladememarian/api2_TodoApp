from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("create_tasks", views.taskM_L),
    path("watch_tasks", views.taskRemain),
]
