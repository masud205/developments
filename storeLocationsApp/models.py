from django.db import models
from django.db import connections

# Create your models here.

class retailers(models.Model):
    retailer_name=models.CharField(max_length=100)

    def __str__(self):
        return self.retailer_name

    class Meta:
        db_table="retailers"

class regions(models.Model):
    region_name=models.CharField(max_length=100)

    def __str__(self):
        return self.region_name

    class Meta:
        db_table="regions"