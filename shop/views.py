from django.http import HttpResponse
from django.template import loader
from .models import Products

def index(request):
    all_products = Products.objects.all()
    template = loader.get_template('shop/index.html')
    context = {
        'all_products' : all_products,
    }
    # html = ''
    # for product in all_products:
    #     url = 'shop/'+str(product.id)+'/'
    #     html+='<a href="'+url+'">'+product.name+'</a><br>'
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    return HttpResponse('<h2>Details for Product ID :'+str(product_id)+' </h2>')
