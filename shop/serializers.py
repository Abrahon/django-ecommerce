from rest_framework import serializers
from .models import Product, Category
class CategorySerilizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerilizers(read_only=True)

    class Meta:
        model = Product
        fields = ['id','name','description', 'price','image','created_at','category']