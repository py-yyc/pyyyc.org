from django.shortcuts import render
from django.views.generic import ListView, DetailView, YearArchiveView, MonthArchiveView

from pyyyc.models import Event


class EventDetail(DetailView):
    model = Event

    def get_object(self, queryset=None):
        date = self.kwargs["date"]
        if queryset is None:
            queryset = self.get_queryset()

        queryset = queryset.filter(date=date)
        return queryset.get()


class EventList(ListView):
    model = Event
    queryset = (
        Event.objects.filter(hidden=False)
        .order_by("-date")
        .prefetch_related("talk_set", "talk_set__presenters")
    )
    template_name = "pyyyc/home.html"


class EventYearArchive(YearArchiveView):
    queryset = Event.objects.filter(hidden=False)
    date_field = "date"
    make_object_list = True
    allow_future = True


class EventMonthArchive(MonthArchiveView):
    queryset = Event.objects.filter(hidden=False)
    date_field = "date"
    make_object_list = True
    allow_future = True


def view_artifact(request, date, file):
    return render(request, "pyyyc/artifact_view.html")
