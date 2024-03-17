"""Defines URL patterns for iris_predict_app."""

from django.urls import path
from . import views

app_name = "iris_predict_app"

urlpatterns = [
    path("", views.predict, name="predict"),
]
