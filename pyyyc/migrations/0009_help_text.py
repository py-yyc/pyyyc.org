from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0008_meetup_link_override"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="meetup_link_override",
            field=models.URLField(
                blank=True,
                help_text="\n            Override the default meetup link generated from the meetup ID.\n        ",
                null=True,
            ),
        ),
    ]
