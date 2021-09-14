from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def storeLocations(request):
    return render(request, 'storeLocations.html');