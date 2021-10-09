from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0005_add_slides_media"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="description_postamble",
            field=models.TextField(
                blank=True,
                default="",
                help_text="\n            If talks are defined for the event, show this info after the talk\n            details. Raw HTML is allowed, and will be sanitized prior to\n            display.\n        ",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="description_preamble",
            field=models.TextField(
                blank=True,
                default="",
                help_text="\n            If talks are defined for the event, show this info before the talk\n            details. Raw HTML is allowed, and will be sanitized prior to\n            display.\n        ",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(
                blank=True,
                default="",
                help_text="\n            Meetup description; only displayed if no talks are defined for this\n            event. Raw HTML is allowed, and will be sanitized prior to display.\n        ",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="hidden",
            field=models.BooleanField(
                default=False,
                help_text="\n            Don’t show this event on the website. Useful for events that were\n            imported from the meetup API, but aren’t meetups or never actually\n            happened.\n        ",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="meetup_api_json",
            field=models.TextField(
                help_text="This can be auto-populated by an import script"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="meetup_id",
            field=models.CharField(
                help_text="Could be used to link to the Meetup website",
                max_length=20,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="meetup_link",
            field=models.URLField(
                blank=True,
                help_text="\n            Override the default meetup link generated from the meetup ID. \n        ",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="processed",
            field=models.BooleanField(
                default=False,
                help_text="\n            Set this to true when talk and presenter details have been entered.\n            It could be used to filter events needing more data entry.\n        ",
            ),
        ),
        migrations.AlterField(
            model_name="talk",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="\n            Talk description, in raw HTML format. It will be sanitized prior to display.\n        ",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="talk",
            name="slides_media",
            field=models.ForeignKey(
                blank=True,
                help_text="Not yet used.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="pyyyc.talkartifact",
            ),
        ),
    ]
