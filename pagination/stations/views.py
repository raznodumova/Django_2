from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    bus_stations = []
    from django.conf import settings
    with open(settings.BUS_STATION_CSV, newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append(row)
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)


    context = {
        'page': page,
        'bus_stations': page.object_list
    }
    return render(request, 'stations/index.html', context)
