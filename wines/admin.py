from django.contrib import admin
from .models import Winery, Region, Wine


# class WineAdminInline(admin.TabularInline):
#     model = Wine
#     list_display = ("slug")
#     # readonly_fields = ("lineitem_total",)

# class RegionAdmin(admin.ModelAdmin):
#     inlines = (WineAdminInline,)
admin.site.register(Region) #multiselect - wine.slugs
 
class WineryAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'name')
    ordering = ('name', )



class WineAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
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


    ordering = ('pk', 'vintage', 'region', 'winery')
    
admin.site.register(Wine, WineAdmin)
admin.site.register(Winery, WineryAdmin)
