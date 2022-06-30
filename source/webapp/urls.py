from django.contrib import admin
from django.urls import path

from webapp.views import create_task

urlpatterns = [
    path("", create_task)
]
