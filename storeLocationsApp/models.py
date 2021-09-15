from django.db import models
from django.db import connections

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
