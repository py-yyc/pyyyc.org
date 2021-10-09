from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from django.db.models import Count
from django.forms import ModelForm, Textarea, TextInput, PasswordInput

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


class EventAdmin(ModelAdmin):
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


class TalkAdmin(ModelAdmin):
    list_display = (
        "presenter",
        "title",
        "date",
        "description",
        "has_slides_link",
        "has_code_link",
    )

    def has_code_link(self, obj):
        return bool(obj.code_link)

    has_code_link.short_description = "Code?"

    def has_slides_link(self, obj):
        return bool(obj.code_link)

    has_slides_link.short_description = "Slides?"


admin.site.register(Talk, TalkAdmin)


class TalkSummaryInline(StackedInline):
    model = Talk
    fields = ("title", "date", "description")
    readonly_fields = ("title", "date", "description")
    extra = 0

    can_delete = False
    show_change_link = True

    def has_add_permission(self, request, obj):
        return False


class PresenterAdmin(ModelAdmin):
    list_display = ("name", "talk_count")
    inlines = [TalkSummaryInline]

    def talk_count(self, obj):
        return obj.talk_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(talk_count=Count("talk"))
        return queryset


admin.site.register(Presenter, PresenterAdmin)

admin.site.register(TalkArtifact)
