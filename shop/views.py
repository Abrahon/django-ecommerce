from django.shortcuts import render
from rest_framework import generics,filters
from .models import Product
from .serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filters_fields = ['category']
    search_fields = ['name','description']
    
