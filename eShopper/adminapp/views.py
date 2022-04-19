from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, AdminUserProfileForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    content = {
        'title': 'Admin | Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'adminapp/admin-users-read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    content = {
        'title': 'Admin | Регистрация',
        'form': form
    }
    return render(request, 'adminapp/admin-users-create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = AdminUserProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = AdminUserProfileForm(instance=user_select)
    content = {
        'title': 'Admin | Обновление данных',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()

    return HttpResponseRedirect(reverse('adminapp:admin_users'))
