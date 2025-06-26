import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from shop.models import Product 

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout(request):
    try:
        
        product = Product.objects.first()

        if not product:
            return HttpResponse("No product found")

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.name,
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/payments/success/',
            cancel_url='http://127.0.0.1:8000/payments/cancel/',
        )
        return redirect(checkout_session.url, code=303)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def success(request):
    return HttpResponse(" Payment successful.")


def cancel(request):
    return HttpResponse(" Payment canceled.")

