from django.contrib import admin
from .models import (
    Product,
    Seller,
    Category,
    Review,
)
# Register your models here.


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'seller', 'description', 'category', 'price']
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Seller)
class BrandsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
    ]
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Review)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'text',
    ]
    readonly_fields = ['date_created', 'date_updated']