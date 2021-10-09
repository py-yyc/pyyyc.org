from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0010_add_simple_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="meetup_api_json",
            field=models.TextField(
                blank=True,
                help_text="This can be auto-populated by an import script",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="meetup_id",
            field=models.CharField(
                blank=True,
                help_text="Could be used to link to the Meetup website",
                max_length=20,
                null=True,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalevent",
            name="meetup_api_json",
            field=models.TextField(
                blank=True,
                help_text="This can be auto-populated by an import script",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalevent",
            name="meetup_id",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="Could be used to link to the Meetup website",
                max_length=20,
                null=True,
            ),
        ),
    ]
