import bleach
from django.db import models
from django.utils.safestring import mark_safe

# A lot of this content was originally imported from the meetup API.
from simple_history.models import HistoricalRecords

SAFE_TAGS_FOR_DESCRIPTIONS = [
    "p",
    "br",
    "hr",
    "b",
    "i",
    "a",
    "img",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
]

SAFE_ATTRIBUTES_FOR_DESCRIPTIONS = {"img": ["src"], "a": ["href"]}


def sanitize_html(raw_html):
    return mark_safe(
        bleach.clean(
            raw_html,
            tags=SAFE_TAGS_FOR_DESCRIPTIONS,
            attributes=SAFE_ATTRIBUTES_FOR_DESCRIPTIONS,
            protocols=["https"],
        )
    )


class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField()
    description = models.TextField(
        default="",
        blank=True,
        help_text="""
            Meetup description; only displayed if no talks are defined for this
            event. Raw HTML is allowed, and will be sanitized prior to display.
        """,
    )
    description_preamble = models.TextField(
        default="",
        blank=True,
        help_text="""
            If talks are defined for the event, show this info before the talk
            details. Raw HTML is allowed, and will be sanitized prior to
            display.
        """,
    )
    description_postamble = models.TextField(
        default="",
        blank=True,
        help_text="""
            If talks are defined for the event, show this info after the talk
            details. Raw HTML is allowed, and will be sanitized prior to
            display.
        """,
    )
    meetup_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text="Could be used to link to the Meetup website",
    )
    meetup_link_override = models.URLField(
        null=True,
        blank=True,
        help_text="""
            Override the default meetup link generated from the meetup ID.
        """,
    )
    meetup_api_json = models.TextField(
        blank=True,
        null=True,
        help_text="This can be auto-populated by an import script",
    )
    video_link = models.URLField(
        null=True,
        blank=True,
        help_text="""
            A link to a video of the entire meetup, as opposed to just one talk.
        """,
    )
    hidden = models.BooleanField(
        default=False,
        help_text="""
            Don’t show this event on the website. Useful for events that were
            imported from the meetup API, but aren’t meetups or never actually
            happened.
        """,
    )
    processed = models.BooleanField(
        default=False,
        help_text="""
            Set this to true when talk and presenter details and slide links
            have all been entered.
        """,
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["-date"]

    def html_description(self):
        return sanitize_html(self.description)

    def html_preamble(self):
        return sanitize_html(self.description_preamble)

    def html_postamble(self):
        return sanitize_html(self.description_postamble)

    def meetup_link(self):
        if self.meetup_link_override:
            return self.meetup_link_override
        if self.meetup_id:
            return f"https://www.meetup.com/py-yyc/events/{self.meetup_id}/"
        return None

    def __str__(self):
        return f"{'X ' if self.hidden else ''}{self.date}: {self.name}"


class Presenter(models.Model):
    name = models.CharField(max_length=50)

    last_name = models.CharField(
        max_length=50,
        default="",
        blank=True,
        help_text="""
            Used in the admin for disambiguation; not currently displayed on the
            website for privacy reasons.
        """,
    )

    history = HistoricalRecords()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}{' ' + self.last_name if self.last_name else ''}"


class TalkArtifact(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()


class Talk(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(
        null=True,
        blank=True,
        help_text="""
            Talk description, in raw HTML format. It will be sanitized prior to display.
        """,
    )
    order = models.FloatField(
        null=True,
        blank=True,
        help_text="""
            Can be used to change the order of talks in an event.
        """,
    )

    slides_link = models.URLField(null=True, blank=True)
    slides_media = models.ForeignKey(
        TalkArtifact,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        help_text="Not yet used.",
    )
    code_link = models.URLField(null=True, blank=True)
    blog_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    # A manual through model can have a better admin display than
    # `Talk-presenter relationship: Talk_presenters object (32)`, but requires
    # extra work to make it inline.
    #
    # Might be needed if wanting to allow manual presenter order for a talk.
    presenters = models.ManyToManyField(Presenter, related_name="talks")
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    history = HistoricalRecords()

    class Meta:
        ordering = ["order", "id"]

    def html_description(self):
        return sanitize_html(self.description)

    @property
    def date(self):
        return self.event.date

    @property
    def presenter_list(self):
        return ", ".join(p.name for p in self.presenters.all())

    def __str__(self):
        return f"{self.title}, {self.presenter_list} {self.event.date}"
