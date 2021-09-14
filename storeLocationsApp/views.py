from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers

# Create your views here.

def all_retailers(request):
    results=retailers.objects.all()
    return render(request, 'storeLocations.html',{"retailers":results});