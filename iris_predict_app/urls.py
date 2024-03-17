"""Defines URL patterns for iris_predict_app."""

from django.urls import path
from . import views

app_name = "iris_predict_app"

urlpatterns = [
    path("", views.predict, name="predict"),
    path("iris_predict_app/", views.predict_chances, name="submit_prediction"),
    path('results/', views.view_results, name='results'),
]
