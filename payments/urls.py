
from django .urls import path
from .views import create_checkout,success,cancel

urlpatterns = [
    path('checkout/', create_checkout, name='checkout'),
    path('success/',success, name='payment_success'),
    path('cancel/', cancel, name='payment-cancel'),
]
