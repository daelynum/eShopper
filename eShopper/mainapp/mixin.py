from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.decorators import method_decorator
from django.views.generic.base import View, ContextMixin

from mainapp.models import Product


class CustomDispatchMixin(View):

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomDispatchMixin, self).dispatch(request, *args, **kwargs)


class CustomLoginDispatchMixin(View):
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CustomLoginDispatchMixin, self).dispatch(request, *args, **kwargs)


class BaseClassContextMixin(ContextMixin):
    title = ''

    def get_context_data(self, **kwargs):
        context = super(BaseClassContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class UserDispatchMixin(View):

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDispatchMixin, self).dispatch(request, *args, **kwargs)
