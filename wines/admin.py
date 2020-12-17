from django.contrib import admin
from .models import Winery, Region, Wine

class WineryAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'name')
    ordering = ('name', )

admin.site.register(Winery, WineryAdmin)


admin.site.register(Region)

class WineAdmin(admin.ModelAdmin):
    list_display = (
        'winery',
        'name',
        'wtype',
        'list_price',
        'discounted_price',
        'vintage',
        'region',
    )

    def winery(self, obj):
        return obj.winery

    def region(self, obj):
        return obj.region


    ordering = ('vintage', 'region', 'winery')
    
admin.site.register(Wine, WineAdmin)
