from django.http import Http404
from django.shortcuts import render
from .models import Products
from .models import Recommends

def index(request):
    all_products = Products.objects.exclude(pk= 0)
    context = {'all_products' : all_products}
    return render(request, 'shop/index.html', context)

def detail(request, product_id):
    try:
        # reco = Products.objects.filter(item=product_id)
        reco = Recommends.objects.filter(item=product_id)
        movie = Products.objects.all()[:1].get()
    except Exception:
        raise Http404("No product !!!")
    context = {'product' : reco, 'current' : movie}
    return render(request, 'shop/product.html', context)
