from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html', {'cart': cart})
def cart(request):
    return render(request, 'cart/cart.html')
@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')
