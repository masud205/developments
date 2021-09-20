from django.contrib import admin
from .models import retailers, regions, municipalities, stores

# Register your models here.
admin.site.register(retailers)
admin.site.register(regions)
admin.site.register(municipalities)
admin.site.register(stores)