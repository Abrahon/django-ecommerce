from django.urls import path
from .views import ProductListView
from .views import BookScrapeView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('books/', BookScrapeView.as_view(), name='book-scrape'),
]