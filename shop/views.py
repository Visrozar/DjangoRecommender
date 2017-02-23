from django.http import Http404
from django.shortcuts import render
from .models import Products

def index(request):
    all_products = Products.objects.all()
    context = {'all_products' : all_products}
    return render(request, 'shop/index.html', context)

def kitchen(request):
    products = Products.objects.filter(category = 'kitchen')
    context = {'all_products' : products}
    return render(request, 'shop/index.html', context)

def sports(request):
    products = Products.objects.filter(category = 'sports')
    context = {'all_products' : products}
    return render(request, 'shop/index.html', context)

def electronics(request):
    products = Products.objects.filter(category = 'electronics')
    context = {'all_products' : products}
    return render(request, 'shop/index.html', context)

def clothing(request):
    products = Products.objects.filter(category = 'clothing')
    context = {'all_products' : products}
    return render(request, 'shop/index.html', context)

def detail(request, product_id):
    try:
        product = Products.objects.get(pk=product_id)
    except Exception:
        raise Http404("No product !!!")
    context = {'product' : product}
    return render(request, 'shop/product.html', context)
