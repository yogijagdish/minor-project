from django.contrib import admin
from .models import climate,climate_langtang,climate_tilicho,sensor_tempreture

# customizing the models

class climateAdmin(admin.ModelAdmin):
    list_display = ['weather','description','temp','temp_min','temp_max']
    list_editable = ['temp']
    list_per_page = 5

class tempretureAdmin(admin.ModelAdmin):
    list_display = ['created_at','field1']
    list_editable = ['created_at']
    list_per_page = 5

# Register your models here.

admin.site.register(climate,climateAdmin)
admin.site.register(climate_tilicho,climateAdmin)
admin.site.register(climate_langtang,climateAdmin)
admin.site.register(sensor_tempreture)