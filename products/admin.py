from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity','image']

admin.site.register(Product)