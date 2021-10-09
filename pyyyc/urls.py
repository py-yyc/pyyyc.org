"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import datetime

from django.conf import settings
from django.urls import path, include, register_converter

from pyyyc.views import (
    EventList,
    view_artifact,
)


class DateConverter:
    regex = "[0-9]{4}-[0-9]{2}-[0-9]{2}"

    def to_python(self, value):
        dt = datetime.datetime.strptime(value, "%Y-%m-%d")
        return dt.date()

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")


register_converter(DateConverter, "date")

urlpatterns = [
    path("", EventList.as_view()),
    # artifact stuff is still a WIP
    path("presentations/<date:date>/<file>", view_artifact),
]

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns.append(path("__debug__", include(debug_toolbar.urls)))
