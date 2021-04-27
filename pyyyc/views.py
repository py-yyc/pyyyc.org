from django.views.generic import ListView, DetailView, YearArchiveView

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
    queryset = Event.objects.filter(hidden=False).order_by("-date")


class EventYearArchive(YearArchiveView):
    queryset = Event.objects.filter(hidden=False)
    date_field = "date"
    make_object_list = True
    allow_future = True
