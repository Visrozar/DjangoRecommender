from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Products
from .models import Recommends
from .forms import UserForm
from django.contrib.auth.models import User

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

class UserFormView(View):
    form_class = UserForm
    template_name = 'shop/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                user = authenticate(username = username, password = password)
                # if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:index')
            user = form.save(commit = False)
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:index')

        return render(request, self.template_name, {'form': form})
