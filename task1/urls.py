from django.contrib import admin
from django.urls import path
from .views import add_booster, index

app_name = "task1"

urlpatterns = [
    path("", index),
    path("add-boost/", add_booster, name="add_boost"),
]
