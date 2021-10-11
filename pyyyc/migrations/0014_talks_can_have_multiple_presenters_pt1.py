from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0013_add_event_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="talk",
            name="presenters",
            field=models.ManyToManyField(
                related_name="presenters", to="pyyyc.Presenter"
            ),
        ),
        migrations.AlterField(
            model_name="talk",
            name="presenter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="presenter",
                to="pyyyc.presenter",
            ),
        ),
    ]
