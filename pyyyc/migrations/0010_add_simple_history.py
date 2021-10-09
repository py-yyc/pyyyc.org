from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pyyyc", "0009_help_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalTalk",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="\n            Talk description, in raw HTML format. It will be sanitized prior to display.\n        ",
                        null=True,
                    ),
                ),
                ("slides_link", models.URLField(blank=True, null=True)),
                ("code_link", models.URLField(blank=True, null=True)),
                ("blog_link", models.URLField(blank=True, null=True)),
                ("video_link", models.URLField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="pyyyc.event",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "presenter",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="pyyyc.presenter",
                    ),
                ),
                (
                    "slides_media",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        help_text="Not yet used.",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="pyyyc.talkartifact",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical talk",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalPresenter",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical presenter",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalEvent",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("date", models.DateField()),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="\n            Meetup description; only displayed if no talks are defined for this\n            event. Raw HTML is allowed, and will be sanitized prior to display.\n        ",
                    ),
                ),
                (
                    "description_preamble",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="\n            If talks are defined for the event, show this info before the talk\n            details. Raw HTML is allowed, and will be sanitized prior to\n            display.\n        ",
                    ),
                ),
                (
                    "description_postamble",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="\n            If talks are defined for the event, show this info after the talk\n            details. Raw HTML is allowed, and will be sanitized prior to\n            display.\n        ",
                    ),
                ),
                (
                    "meetup_id",
                    models.CharField(
                        db_index=True,
                        help_text="Could be used to link to the Meetup website",
                        max_length=20,
                    ),
                ),
                (
                    "meetup_link_override",
                    models.URLField(
                        blank=True,
                        help_text="\n            Override the default meetup link generated from the meetup ID.\n        ",
                        null=True,
                    ),
                ),
                (
                    "meetup_api_json",
                    models.TextField(
                        help_text="This can be auto-populated by an import script"
                    ),
                ),
                (
                    "hidden",
                    models.BooleanField(
                        default=False,
                        help_text="\n            Don’t show this event on the website. Useful for events that were\n            imported from the meetup API, but aren’t meetups or never actually\n            happened.\n        ",
                    ),
                ),
                (
                    "processed",
                    models.BooleanField(
                        default=False,
                        help_text="\n            Set this to true when talk and presenter details and slide links\n            have all been entered.\n        ",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical event",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
