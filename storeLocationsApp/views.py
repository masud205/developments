from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers, regions, municipalities, stores

# Create your views here.

def get_dropdown_data(request):
    retailerobj = retailers.objects.all()
    regionobj = regions.objects.all()
    municipalobj = municipalities.objects.all()

    if request.method == "POST":
        retail_id = request.POST.get('retailers')
        reg_id = request.POST.get('regions')
        
        #ret_id = retailers.objects.get(retailer_name=retail_name)
        #regid = regions.objects.get(region_name=reg_val)
        municipal = municipalities.objects.filter(region_id=reg_id)
        store = stores.objects.filter(retailer_id = retail_id, municipality_id__in=municipal.values('municipality_id'))
        return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_stores": store});
    else:
        store = stores.objects.all()
        return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_storess": store});


