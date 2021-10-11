from django.db import migrations
from django.db.migrations import RunPython


class Migration(migrations.Migration):

    dependencies = [
        ("pyyyc", "0014_talks_can_have_multiple_presenters_pt1"),
    ]

    def migrate(apps, schema_editor):
        Talk = apps.get_model("pyyyc", "Talk")
        for talk in Talk.objects.all():
            talk.presenters.add(talk.presenter)

    operations = [RunPython(migrate)]
