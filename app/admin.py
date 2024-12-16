from django.contrib import admin
from .models import (
    Product,
    Brand,
    Category,
    Review,
)
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'description', 'category', 'price']
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'text',
    ]
    readonly_fields = ['date_created', 'date_updated']