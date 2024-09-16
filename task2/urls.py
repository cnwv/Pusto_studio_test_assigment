from django.urls import path
from .views import registrate_player, complete_level, get_prize

app_name = "task1"

urlpatterns = [
    path("registration/", registrate_player, name="registration"),
    path("complete-level/", complete_level, name="registration"),
    path("get-prize/", get_prize, name="registration"),
]
