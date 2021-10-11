from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0015_talks_can_have_multiple_presenters_pt2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicaltalk",
            name="presenter",
        ),
        migrations.RemoveField(
            model_name="talk",
            name="presenter",
        ),
        migrations.AlterField(
            model_name="historicalpresenter",
            name="last_name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="\n            Used in the admin for disambiguation; not currently displayed on the\n            website for privacy reasons.\n        ",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="presenter",
            name="last_name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="\n            Used in the admin for disambiguation; not currently displayed on the\n            website for privacy reasons.\n        ",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="talk",
            name="presenters",
            field=models.ManyToManyField(related_name="talks", to="pyyyc.Presenter"),
        ),
    ]
