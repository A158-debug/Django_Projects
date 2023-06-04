from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil

# Create your views here.
def index(request):
    product = Product.objects.all()
    n = len(product)
    n_slides = ceil(n/4)
    params = {'no_of_slides':n_slides, 'range':range(n_slides),'product':product}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/productView.html')

def checkout(request):
    return render(request, 'shop/checkout.html')
