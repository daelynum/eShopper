from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    content = {'title': 'EShopper'}
    return render(request, 'mainapp/index.html', content)


def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    content = {'title': 'EShopper - Products', 'products': products, 'categories': categories}
    return render(request, 'mainapp/products.html', content)
