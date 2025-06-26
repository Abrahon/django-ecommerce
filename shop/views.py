from django.shortcuts import render
from rest_framework import generics,filters
from .models import Product
from .serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filters_fields = ['category']
    search_fields = ['name','description']
    


class BookScrapeView(APIView):
    def get(self, request):
        url = "https://books.toscrape.com/catalogue/page-1.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        books = []
        for h3 in soup.select('article.product_pod h3'):
            title = h3.a['title']
            books.append(title)

        return Response({"books": books})
