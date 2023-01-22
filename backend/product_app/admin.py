from django.contrib import admin
from .models import Product



# product admin 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','date']
    list_display_links = ['name','price','category']
    list_filter = ['category','date']
    search_fields = ['category','name']

admin.site.register(Product, ProductAdmin)
