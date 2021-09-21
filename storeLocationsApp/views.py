from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers, regions, municipalities, stores
from django.core import serializers


# Create your views here.

def get_dropdown_data(request):
    retailerobj = retailers.objects.all()
    regionobj = regions.objects.all()
    municipalobj = municipalities.objects.all()

    if request.method == "POST":
        retail_id = request.POST.get('retailers')
        reg_id = request.POST.get('regions')
        municipal_id = request.POST.get('municipalities')
                
        if reg_id == "---Select Region---" and municipal_id == "---Select Municipality---":
            store = stores.objects.filter(retailer_id = retail_id, municipality_id__in=municipalobj.values('municipality_id')) 

        elif reg_id != "---Select Region---" and municipal_id == "---Select Municipality---":
            municipal = municipalities.objects.filter(region_id=reg_id)
            store = stores.objects.filter(retailer_id = retail_id, municipality_id__in=municipal.values('municipality_id'))

        else:
            store = stores.objects.filter(retailer_id = retail_id, municipality_id = municipal_id)
            store_data = serializers.serialize("json", store)
            print(store_data)

        return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_stores": store_data});
    else:
        store = stores.objects.all()
        return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_all_stores": store});


