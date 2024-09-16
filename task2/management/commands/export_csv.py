import csv
from django.core.management.base import BaseCommand
from django.db.models import OuterRef, Subquery
from task2.models import PlayerLevel, LevelPrize


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        csv_file_path = "player_level_prize_export.csv"
        BATCH_SIZE = 1000

        # Подготовка подзапроса для получения названия приза
        level_prize_subquery = LevelPrize.objects.filter(
            level=OuterRef("level")
        ).values("prize__title")[:1]

        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["player_id", "level_title", "is_completed", "prize_title"])

            queryset = (
                PlayerLevel.objects.annotate(prize_title=Subquery(level_prize_subquery))
                .select_related("player", "level")
                .values(
                    "player__player_id",  # ID игрока
                    "level__title",  # Название уровня
                    "is_completed",  # Пройден ли уровень
                    "prize_title",  # Название полученного приза
                )
            )

            for obj in queryset.iterator(chunk_size=BATCH_SIZE):
                writer.writerow(
                    [
                        obj["player__player_id"],
                        obj["level__title"],
                        obj["is_completed"],
                        obj["prize_title"],
                    ]
                )
            print(f"Data successfully exported to {csv_file_path}")