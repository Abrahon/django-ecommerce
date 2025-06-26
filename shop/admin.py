from django.contrib import admin
from django.contrib import admin
from .models import Product, Category 
# Register your models here.
 

# Optional: Customize how models appear
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
