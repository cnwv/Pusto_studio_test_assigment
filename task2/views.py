import json

from django.http import HttpResponse, Http404

from .models import Player, Level, Prize, PlayerLevel, PlayerPrize, LevelPrize
from django.views.decorators.http import require_POST


@require_POST
def registrate_player(request):
    player = Player().create_player()
    return HttpResponse(f"Player with id {player.pk} has been created")


@require_POST
def complete_level(request):
    data = json.loads(request.body)
    score = data.get("score")
    player = Player.objects.get(pk=data.get("player_id"))
    level = Level.objects.filter(order=data.get("level")).first()
    player_level = PlayerLevel()
    player_level.complete_level(player, level, score)
    return HttpResponse(f"status: level {level.order} complete")


@require_POST
def get_prize(request):
    data = json.loads(request.body)
    player = Player.objects.get(pk=data.get("player_id"))
    level = Level.objects.filter(order=data.get("level")).first()
    player_prize = PlayerPrize()
    if player_level := PlayerLevel.objects.filter(
        player_id=player, level_id=level
    ).first():
        player_prize.get_prize(player=player, player_level=player_level, level=level)
        if player_prize:
            return HttpResponse(f"Player {player} has received prize")
    else:
        raise Http404("Player has not completed level")
