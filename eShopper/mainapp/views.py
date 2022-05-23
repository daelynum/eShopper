from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.base import ContextMixin, View
from django.views.generic.list import MultipleObjectMixin

from mainapp.mixin import BaseClassContextMixin
from mainapp.models import Product, ProductCategory


class IndexTemplateView(TemplateView, BaseClassContextMixin):
    title = 'EShopper'
    template_name = 'mainapp/index.html'

class ProductView(View):
    def get(self, request, page = 1, id_category=None):
        if id_category:
            products = Product.objects.filter(category_id=id_category)
        else:
            products = Product.objects.all()

        pagination = Paginator(products, per_page=2)
        page_num = request.GET.get('page', page)
        try:
            product_pagination = pagination.get_page(page_num)
        except PageNotAnInteger:
            product_pagination = pagination.page(1)
        except EmptyPage:
            product_pagination = pagination.page(pagination.num_pages)
        content = {
            'title': 'Geekshop - Каталог',
            'categories': ProductCategory.objects.all(),
            'products': product_pagination

        }
        return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
