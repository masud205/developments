#from django.db import models
#from django.db import connections
from django.contrib.gis.db import models

# Create your models here.

class retailers(models.Model):
    retailer_id = models.IntegerField(primary_key=True, default=150)
    retailer_name = models.CharField(max_length=100)
    store_type = models.CharField(max_length=100, null=True, blank=True)
    parent_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "retailers"

class regions(models.Model):
    region_id = models.IntegerField(primary_key=True, default=50)
    region_name = models.CharField(max_length=100)
    region_lat = models.FloatField(null=True, blank=True)
    region_long = models.FloatField(null=True, blank=True)
    region_area = models.FloatField(null=True, blank=True)
    region_code = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = "regions"

class municipalities(models.Model):
    municipality_id = models.IntegerField(primary_key=True, default=3000)
    municipality_code = models.CharField(max_length=10)
    region = models.ForeignKey('regions', on_delete=models.SET_NULL, null=True, blank=True)
    municipality_name = models.CharField(max_length=100)
    municipality_area = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    number_of_cars = models.IntegerField(null=True, blank=True)
    avg_income = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "municipalities"

class stores(models.Model):
    store_id = models.IntegerField(primary_key=True, default=99999)
    retailer = models.ForeignKey('retailers', on_delete=models.SET_NULL, null=True, blank=True)
    municipality = models.ForeignKey('municipalities', on_delete=models.SET_NULL, null=True, blank=True)
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=300)
    store_lat = models.FloatField(null=True, blank=True)
    store_long = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "stores"
