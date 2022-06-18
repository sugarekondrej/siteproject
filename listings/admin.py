from django.contrib import admin

# Register your models here.
from . models import Listings


class ListingsAdmin(admin.ModelAdmin):
    list_display=('id','address','is_published','city','price','realtor', 'sqft')
    list_display_links=('id','address')
    list_editable = ('is_published',)
    search_fields = ('id','address','city','price')
admin.site.register(Listings,ListingsAdmin)
