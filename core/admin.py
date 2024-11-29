from django.contrib import admin
from .models import Product, Brand
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ["name", "price", "state", "created"]
    list_filter = ["state", "brand"]
    search_fields = ["name",]
    list_editable = ["price"]


class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ["name", "created"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)