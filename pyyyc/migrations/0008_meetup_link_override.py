from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0007_help_text"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="meetup_link",
            new_name="meetup_link_override",
        ),
    ]
