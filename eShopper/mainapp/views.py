from django.shortcuts import render


def index(request):
    content = {'title': 'EShopper'}
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {'title': 'EShopper - Products'}
    return render(request, 'mainapp/products.html', content)
