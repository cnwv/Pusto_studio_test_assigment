from django.utils import timezone

from django.db import models


class Player(models.Model):
    username = models.CharField(unique=True, null=False, max_length=64)
    first_login_at = models.DateField(auto_now=True, null=True)
    last_login_at = models.DateField(auto_now=True, null=True)
    daily_points = models.IntegerField(default=0, null=False)
    daily_streak = models.IntegerField(default=0, null=False)

    def record_first_login(self):
        if self.first_login_at is None:
            self.first_login_at = timezone.now()
            self.save()

    def record_login(self):
        self.last_login_at = timezone.now()
        self.save()

    def add_daily_point(self):
        self.daily_points += 1
        self.save()

    def up_daily_streak(self):
        self.daily_streak += 1
        self.save()

    def reset_daily_streak(self):
        self.daily_streak = 0
        self.save()

    def add_boost(self, boost, value):
        player_boost, _ = PlayerBoost.objects.get_or_create(
            player=self, boost=boost
        )
        player_boost.value += value
        player_boost.save()
        return player_boost


class Boost(models.Model):
    boost_type = models.CharField(max_length=50)


class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("player", "boost")

    def __str__(self):
        return f"{self.player} - {self.boost} ({self.value})"
