from django.db import models
from django.db import connections

# Create your models here.

class retailers(models.Model):
    retailer_name=models.CharField(max_length=100)
    class Meta:
        db_table="retailers"