from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers, regions

# Create your views here.

def get_data(request):
    retailerobj = retailers.objects.all()
    regionobj = regions.objects.all()
    return render(request, 'storeLocations.html',{"retailers":retailerobj, "regions":regionobj});
