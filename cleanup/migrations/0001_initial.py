# Generated by Django 5.1.1 on 2024-09-27 06:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cleanup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("arrival_photo", models.ImageField(upload_to="photos/arrival/")),
                (
                    "arrival_timestamp",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("arrival_latitude", models.FloatField()),
                ("arrival_longitude", models.FloatField()),
                ("coast_name", models.CharField(max_length=255)),
                ("coast_length", models.FloatField()),
                ("litter_bags_count", models.IntegerField()),
                (
                    "main_litter_type",
                    models.IntegerField(
                        choices=[
                            (1, "Fishing Gear"),
                            (2, "Buoys"),
                            (3, "Household Waste"),
                            (4, "Large Illegal Dumping"),
                            (5, "Vegetation"),
                        ]
                    ),
                ),
                (
                    "completion_photo_coast",
                    models.ImageField(upload_to="photos/completion/coast/"),
                ),
                (
                    "completion_photo_collection",
                    models.ImageField(upload_to="photos/completion/collection/"),
                ),
            ],
        ),
    ]
