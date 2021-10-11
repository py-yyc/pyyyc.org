from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0017_event_sort"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="talk",
            options={"ordering": ["order", "id"]},
        ),
        migrations.AddField(
            model_name="historicaltalk",
            name="order",
            field=models.FloatField(
                blank=True,
                help_text="\n            Can be used to change the order of talks in an event.\n        ",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="talk",
            name="order",
            field=models.FloatField(
                blank=True,
                help_text="\n            Can be used to change the order of talks in an event.\n        ",
                null=True,
            ),
        ),
    ]
