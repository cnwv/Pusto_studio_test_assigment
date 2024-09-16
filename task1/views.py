from django.http import HttpResponse
from django.shortcuts import render
from .models import Boost, Player

# add decorator post request
"""
class Player(models.Model):
    username = models.CharField(unique=True, null=False, max_length=64)
    first_login_at = models.DateField(auto_now=True, null=True)
    daily_points = models.IntegerField(default=0, null=False)
    daily_streak = models.IntegerField(default=0, null=False)


class Boost(models.Model):
    BOOST_TYPES = [
        ("speed", "Скорость"),
        ("shield", "Щит"),
    ]

    player_id = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="boosts"
    )
    boost_type = models.CharField(max_length=10, choices=BOOST_TYPES)
    value = models.IntegerField()
    expires_at = models.DateTimeField(null=True, blank=True)

    # add method to add boost to player
    def add_boost(self, player_id: int, boost_type: str, value: int):
        boost = Boost.objects.create(
            player_id=player_id, boost_type=boost_type, value=value
        )
        return {"status": "ok"}
"""


# def add_boost(request, player_id: int, boost_type: str, value: int):
#     player_id = Player.objects.get(id=player_id)
#     boost = Boost.objects.create(
#         player_id=player_id,
#         boost_type=request.POST["boost_type"],
#         value=request.POST["value"],
#     )


def index(request):
    player = Player.objects.get(id=1)
    player.record_first_login()
    return HttpResponse("HI")


def add_booster(request):
    boost = Boost.add_boost(player_id=1, boost_type="speed", value=10)
    return HttpResponse("HI")
