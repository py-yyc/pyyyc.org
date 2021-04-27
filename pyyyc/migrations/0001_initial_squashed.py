# Generated by Django 3.2 on 2021-04-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("pyyyc", "0001_initial"),
        ("pyyyc", "0002_auto_20210427_0050"),
        ("pyyyc", "0003_event_description"),
        ("pyyyc", "0004_event_hidden"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=500)),
                ("date", models.DateField()),
                ("meetup_id", models.CharField(max_length=20, unique=True)),
                ("meetup_api_json", models.TextField()),
                ("description", models.TextField(default="")),
                ("hidden", models.BooleanField(default=False)),
            ],
        ),
    ]