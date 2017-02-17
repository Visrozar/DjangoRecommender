from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

def index(request):
    all_products = Products.objects.all()
    context = {'all_products' : all_products}
    return render(request, 'shop/index.html', context)

def detail(request, product_id):
    return HttpResponse('<h2>Details for Product ID :'+str(product_id)+' </h2>')
