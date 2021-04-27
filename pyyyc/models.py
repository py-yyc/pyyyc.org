import bleach
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

SAFE_TAGS_FOR_DESCRIPTIONS_FROM_MEETUP = ["p", "br", "b", "i", "a"]


class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField()
    description = models.TextField(default="", blank=True)
    meetup_id = models.CharField(max_length=20, unique=True)
    meetup_api_json = models.TextField()
    meetup_link = models.URLField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
    # Set by a staff member when talks and presenters have been updated
    processed = models.BooleanField(default=False)

    def html_description(self):
        return mark_safe(
            bleach.clean(self.description, tags=SAFE_TAGS_FOR_DESCRIPTIONS_FROM_MEETUP)
        )

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"date": self.date})

    def __str__(self):
        return f"{self.date}: {self.name}"


class Presenter(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Talk(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)

    slides_links = models.URLField(null=True, blank=True)
    code_link = models.URLField(null=True, blank=True)
    blog_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)

    presenter = models.ForeignKey(Presenter, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    @property
    def date(self):
        return self.event.date

    def __str__(self):
        return f"{self.title}, {self.presenter.name} {self.event.date}"
