import pytz

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    # Программируем здесь
    timezone.activate("Europe/Moscow")
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": visit.get_duration,
            "is_strange": visit.is_long,
        }
        for visit in active_visits
    ]

    context = {"non_closed_visits": non_closed_visits}  # не закрытые посещения
    return render(request, "storage_information.html", context)
