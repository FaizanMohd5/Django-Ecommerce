from django.shortcuts import render

from product.models import Product
# Create your views here.

def frontPage(request):
   products = Product.objects.all()[0:8]

   return render(request, 'core/frontpage.html', {'products':products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'core/shop.html', {'products':products})

