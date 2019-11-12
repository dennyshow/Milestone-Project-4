from django.shortcuts import render
from products.models import Product

# Create your views here.

def to_search(request):
    products = Product.objects.filter(product_name__icontains=request.GET['q'])
    return render(request, "products.html", {'products': products})