from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0006_add_pre_and_postamble"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="processed",
            field=models.BooleanField(
                default=False,
                help_text="\n            Set this to true when talk and presenter details and slide links\n            have all been entered.\n        ",
            ),
        ),
    ]
