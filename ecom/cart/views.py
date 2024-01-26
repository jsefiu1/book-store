from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products": cart_products})



def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        #  Get stuff
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product)
        cart_quantity = cart.__len__()

        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass