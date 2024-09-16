from django.db import models
from django.utils import timezone


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.player_id}"

    def create_player(self):
        self.save()
        return self


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.title

    def add_level(self, title, order):
        self.title = title
        self.order = order
        self.save()
        return self


class Prize(models.Model):
    title = models.CharField(max_length=100)

    def add_prize(self, title):
        self.title = title
        self.save()
        return self


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, to_field="order")
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("player", "level")

    def complete_level(self, player, level, score):
        self.player = player
        self.level = level
        self.completed = timezone.now()
        self.is_completed = True
        self.score = score
        self.save()
        return self


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, to_field="order")
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    # received = models.DateField()

    class Meta:
        unique_together = ("level", "prize")

    def __str__(self):
        return f"{self.level} - {self.prize}"

    def set_level_prize(self, level, prize):
        self.level = level
        self.prize = prize
        self.save()
        return self


class PlayerPrize(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, to_field="order")
    received_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("player", "level")

    def __str__(self):
        return f"{self.player} - {self.level}"

    def get_prize(self, player, player_level: PlayerLevel, level):
        if player_level.is_completed:
            self.player = player
            self.level = level
            self.received_at = timezone.now()
            self.save()
            return self
        else:
            return None
