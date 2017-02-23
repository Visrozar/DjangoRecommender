from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

def index(request):
    all_products = Products.objects.all()
    kitchen_products = Products.objects.filter(category = 'kitchen')
    context = {'all_products' : all_products}
    return render(request, 'shop/index.html', context)

def detail(request, product_id):
    product = Products.objects.get(pk=product_id)
    context = {'product' : product}
    return render(request, 'shop/product.html', context)
