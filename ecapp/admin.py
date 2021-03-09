from django.contrib import admin
from ecapp.models import Products

# Register your models here.

class Product_admin(admin.ModelAdmin):  
    list_display=['name','original_price','discounted_price','category','description','image']


admin.site.register(Products,Product_admin)