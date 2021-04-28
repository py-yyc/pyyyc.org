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


def home(request):
    events = Event.objects.filter(hidden=False).order_by("-date")[:2]
    return render(request, "pyyyc/home.html", context={"event_list": events})


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
