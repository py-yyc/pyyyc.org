import json
from argparse import ArgumentParser

from django.core.management import BaseCommand

from pyyyc.models import Event


class Command(BaseCommand):
    help = """Create database entries from JSON file"""

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("--json-file", required=True)

    def handle(self, *args, **options):
        db_events = Event.objects.in_bulk(field_name="meetup_id")

        with open(options["json_file"], "r") as f:
            data = json.load(f)

            for json_event in data:
                meetup_id = json_event["id"]
                event = db_events.get(meetup_id, None)

                needs_save = False
                if event is None:
                    event = Event()
                    needs_save = True
                    event.meetup_id = meetup_id

                if not event.name:
                    event.name = json_event["name"]
                    needs_save = True
                if not event.date:
                    event.date = json_event["local_date"]
                    needs_save = True
                if not event.description:
                    event.description = json_event.get("description", "")
                    needs_save = True
                if not event.meetup_api_json:
                    event.meetup_api_json = json.dumps(
                        json_event, ensure_ascii=False, indent=2
                    )
                    needs_save = True

                if needs_save:
                    event.save()
                    print("Saved", event)
