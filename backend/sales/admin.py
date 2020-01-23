from django.contrib import admin
from .models import ProductModel as Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]


admin.site.register(Product, ProductAdmin)
