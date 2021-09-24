from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers, regions, municipalities, stores
from django.core import serializers
import json
import simplejson


# Create your views here.

def get_dropdown_data(request):
     retailerobj = retailers.objects.all()
     regionobj = regions.objects.all()
     municipalobj = municipalities.objects.all()

     if request.method == "POST":
        retail_id = request.POST.get('retailers')
        reg_id = request.POST.get('regions')
        municipal_id = request.POST.get('municipalities')
        
        #get selected retailer information
        try:
            retailer = retailers.objects.get(retailer_id=retail_id)
        except ValueError:
            retailer = {'retailer_name':'No retailer selected'}

        #get selected region information
        try:
            region = regions.objects.get(region_id=reg_id)
        except ValueError:
            region = {'region_name':'All regions'}
        
        #get selected municipality information
        try:
            municipality = municipalities.objects.get(municipality_id=municipal_id)
        except ValueError:
            municipality = {'municipality_name':'All municipalities'}
                
        if reg_id == "---Select Region---" and municipal_id == "---Select Municipality---":
            store = stores.objects.filter(retailer_id = retail_id, municipality_id__in=municipalobj.values('municipality_id')) 
            store_data = serializers.serialize("json", store)

        elif reg_id != "---Select Region---" and municipal_id == "---Select Municipality---":
            municipal = municipalities.objects.filter(region_id=reg_id)
            store = stores.objects.filter(retailer_id = retail_id, municipality_id__in=municipal.values('municipality_id'))
            store_data = serializers.serialize("json", store)

        else:
            store = stores.objects.filter(retailer_id = retail_id, municipality_id = municipal_id)
            store_data = serializers.serialize("json", store)
            #store_js = simplejson.loads(store_data)
            #print(store_js)
            #print(store_data)
            #print(store)
            
            #print(store_js[0]['fields']['store_address'])

        return render(request, 'storeLocations.html', {"selected_retailer": retailer, "selected_region": region, "selected_municipal": municipality, "retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_stores": store_data});
     else:
        store = stores.objects.all()
        return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_stores": store});


