from django.shortcuts import render
from django.http import HttpResponse
from storeLocationsApp.models import retailers, regions, municipalities, stores
from django.core import serializers
import json
import simplejson
import xlwt
import datetime
from django.db import connection


# Create your views here.

def get_dropdown_data(request):
     global store
     retailerobj = retailers.objects.filter(retailer_id__in=stores.objects.values('retailer_id'))
     regionobj = regions.objects.all()
     municipalobj = municipalities.objects.all()

     if request.method == "POST":
        retail_id = request.POST.get('retailers')
        reg_id  = request.POST.get('regions')
        municipal_id  = request.POST.get('municipalities')
        
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

        return render(request, 'storeLocations.html', {"selected_retailer": retailer, "selected_region": region, "selected_municipal": municipality, 
                                                       "retailers": retailerobj, "regions": regionobj, "municipalities": municipalobj, "find_stores_str": store, "find_stores_json": store_data});
     else:
        store = stores.objects.all()
        return render(request, 'storeLocations.html', {"retailers": retailerobj, "regions": regionobj,
                                                   "municipalities": municipalobj, "find_all_stores": store});


def export_excel(request):
    #global store
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Stores' + \
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook()#(encoding='ISO_8859_1')
    ws = wb.add_sheet('Stores')
    
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columns = ['store_id', 'retailer_id', 'municipality_id', 'store_name', 'retailer_name', 'municipality_name', 'store_address', 'store_lat', 'store_long']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
  
    font_style = xlwt.XFStyle()
    
    #print(store)
    stores_info = store.select_related('retailer', 'municipality').order_by('municipality') ## joining with retailers and municipalities table using foreign keys retailer_id and municipality_id

    rows = stores_info.values_list('store_id', 'retailer_id', 'municipality_id', 'store_name', 'retailer__retailer_name', 'municipality__municipality_name', 'store_address', 'store_lat', 'store_long')

    #rows = store.values_list('store_id', 'retailer_id', 'municipality_id', 'store_name', 'store_address', 'store_lat', 'store_long')

    for row in rows:
        row_num+=1
       
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    
    wb.save(response)

    return response