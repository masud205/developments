from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers, regions, municipalities

# Create your views here.

def get_data(request):
    retailerobj = retailers.objects.all()
    regionobj = regions.objects.all()
    municipalobj = municipalities.objects.all()
    return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj});
