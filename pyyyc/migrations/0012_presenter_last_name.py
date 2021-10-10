from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0011_make_some_meetup_fields_optional"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpresenter",
            name="last_name",
            field=models.CharField(
                default="",
                help_text="\n            Used in the admin for disambiguation; not currently displayed on the\n            website for privacy reasons.\n        ",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="presenter",
            name="last_name",
            field=models.CharField(
                default="",
                help_text="\n            Used in the admin for disambiguation; not currently displayed on the\n            website for privacy reasons.\n        ",
                max_length=50,
            ),
        ),
    ]
