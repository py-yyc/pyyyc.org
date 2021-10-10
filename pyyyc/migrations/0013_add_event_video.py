from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0012_presenter_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="video_link",
            field=models.URLField(
                blank=True,
                help_text="\n            A link to a video of the entire meetup, as opposed to just one talk.\n        ",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalevent",
            name="video_link",
            field=models.URLField(
                blank=True,
                help_text="\n            A link to a video of the entire meetup, as opposed to just one talk.\n        ",
                null=True,
            ),
        ),
    ]
