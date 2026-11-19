from django.contrib import admin
from .models import Supplier, Category, Product
# Register your models here.

admin.site.register(Supplier)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'supplier', 'category', 'quantity_in_stock')
    search_filter = ('name', 'sku')
    list_filter = ('category', 'supplier')