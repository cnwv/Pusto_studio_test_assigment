from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("task1/", include("task1.urls", namespace="task1")),
    path("task2/", include("task2.urls", namespace="task2")),
]
