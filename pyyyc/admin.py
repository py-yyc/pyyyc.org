from django.contrib import admin
from django.contrib.admin import StackedInline
from django.db.models import Count
from django.forms import ModelForm, Textarea
from django.urls import reverse
from django.utils.html import format_html
from simple_history.admin import SimpleHistoryAdmin

from pyyyc.models import Event, Talk, Presenter, TalkArtifact


class TalkInline(StackedInline):
    model = Talk
    extra = 1

    can_delete = False
    show_change_link = True


# https://stackoverflow.com/questions/18738486/control-the-size-textarea-widget-look-in-django-admin
class EventModelForm(ModelForm):
    class Meta:
        model = Event
        exclude = []
        widgets = {"meetup_api_json": Textarea(attrs={"readonly": "readonly"})}


class EventAdmin(SimpleHistoryAdmin):
    form = EventModelForm
    list_display = ("name", "yyyymmdd", "talk_count", "processed")
    list_filter = ("processed",)
    inlines = [TalkInline]

    def yyyymmdd(self, obj):
        return obj.date.strftime("%Y-%m-%d")

    def talk_count(self, obj):
        return obj.talk_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(talk_count=Count("talk"))
        return queryset


admin.site.register(Event, EventAdmin)


class TalkAdmin(SimpleHistoryAdmin):
    list_display = (
        "title",
        "date",
        "presenter_list",
        "description",
        "has_slides_link",
        "has_code_link",
    )

    @admin.display(description="Code?", boolean=True)
    def has_code_link(self, obj):
        return bool(obj.code_link)

    @admin.display(description="Slides?", boolean=True)
    def has_slides_link(self, obj):
        return bool(obj.code_link)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("event", "presenters")


admin.site.register(Talk, TalkAdmin)


class TalkSummaryInline(StackedInline):
    def info(self, obj):
        edit_url = reverse("admin:pyyyc_talk_change", args=[obj.id])

        return format_html(
            "<a href={url}>{date}</a> {title}",
            url=edit_url,
            date=obj.talk.event.date,
            title=obj.talk.title,
        )

    @admin.display(description="description")
    def description(self, obj):
        return obj.talk.description

    model = Presenter.talks.through
    fields = (
        "info",
        "description",
    )
    readonly_fields = fields
    extra = 0

    can_delete = False
    show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def get_queryset(self, request):
        return (
            super().get_queryset(request).prefetch_related("talk__event", "presenter")
        )


class PresenterAdmin(SimpleHistoryAdmin):
    list_display = ("name", "last_name", "talk_count")
    inlines = [TalkSummaryInline]

    def talk_count(self, obj):
        return obj.talk_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(talk_count=Count("talks"))
        return queryset


admin.site.register(Presenter, PresenterAdmin)
