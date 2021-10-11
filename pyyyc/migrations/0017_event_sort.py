from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0016_talks_can_have_multiple_presenters_pt3"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"ordering": ["-date"]},
        ),
    ]
