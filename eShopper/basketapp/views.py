from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.mixin import CustomLoginDispatchMixin
from mainapp.models import Product
from django.views.generic.base import View


class BasketAddView(CustomLoginDispatchMixin, View):
    def get(self, request, id):
        user_select = request.user
        product = Product.objects.get(id=id)
        baskets = Basket.objects.filter(user=user_select, product=product)

        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=user_select, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @login_required
# def basket_add(request, id):
#     user_select = request.user
#     product = Product.objects.get(id=id)
#     baskets = Basket.objects.filter(user=user_select, product=product)
#
#     if baskets:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#     else:
#         Basket.objects.create(user=user_select, product=product, quantity=1)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class BasketRemoveView(CustomLoginDispatchMixin, View):
    def get(self, request, basket_id):
        Basket.objects.get(id=basket_id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @login_required
# def basket_remove(request, basket_id):
#     Basket.objects.get(id=basket_id).delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class BasketEditView(CustomLoginDispatchMixin, View):
    def get(self, request, id_basket, quantity):
        if is_ajax(request=request):
            basket = Basket.objects.get(id=id_basket)
            if quantity > 0:
                basket.quantity = quantity
                basket.save()
            else:
                basket.delete()
            basket = Basket.objects.filter(user=request.user)
            content = {
                'basket': basket,
            }
            result = render_to_string('basket/basket.html', content)
            return JsonResponse({'result': result})

# @login_required
# def basket_edit(request, id_basket, quantity):
#     if is_ajax(request=request):
#         basket = Basket.objects.get(id=id_basket)
#         if quantity > 0:
#             basket.quantity = quantity
#             basket.save()
#         else:
#             basket.delete()
#         basket = Basket.objects.filter(user=request.user)
#         content = {
#             'basket': basket,
#         }
#         result = render_to_string('basket/basket.html', content)
#         return JsonResponse({'result': result})
