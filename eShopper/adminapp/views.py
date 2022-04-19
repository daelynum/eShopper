from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from adminapp.forms import UserAdminRegisterForm, AdminUserProfileForm
from authapp.models import User
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView, CreateView

from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = "Admin | Главная"


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = "Admin | Пользователи"
    context_object_name = 'users'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    title = 'Admin | Регистрация'
    form_class = UserAdminRegisterForm
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('adminapp:admin_users')


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    title = 'Admin | Обновление данных'
    form_class = AdminUserProfileForm
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_users')


class DeleteUserView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
