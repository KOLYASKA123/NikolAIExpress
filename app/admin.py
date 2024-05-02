from django.contrib import admin
from .models import (
    Products,
    Brands,
    Categories,
    SubCategories,
    Feedbacks,
)
# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'description', 'category', 'price']
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
    ]
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'parent',
    ]

@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'text',
    ]
    readonly_fields = ['date_created', 'date_updated']