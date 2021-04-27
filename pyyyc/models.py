import bleach
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

SAFE_TAGS_FOR_DESCRIPTIONS_FROM_MEETUP = ["p", "br", "b", "i", "a"]


class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField()
    description = models.TextField(default="")
    meetup_id = models.CharField(max_length=20, unique=True)
    meetup_api_json = models.TextField()
    hidden = models.BooleanField(default=False)

    def html_description(self):
        return mark_safe(
            bleach.clean(self.description, tags=SAFE_TAGS_FOR_DESCRIPTIONS_FROM_MEETUP)
        )

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"date": self.date})

    def __str__(self):
        return f"{self.date}: {self.name}"
