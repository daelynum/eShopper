import django.contrib.auth.context_processors
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket
from mainapp.mixin import CustomLoginDispatchMixin
from django.views.generic.base import View


class LoginView(View):
    def get(self, request):

        form = UserLoginForm()
        content = {
            'title': 'Авторизация',
            'form': form
        }
        return render(request, 'authapp/login.html', content)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        # проверяем правильно ли заполнены поля
        if form.is_valid():
            # получаем пароль и логин
            username = request.POST.get('username')
            password = request.POST.get('password')

            # если данные действительны, возвращаем объект пользователя.
            user = auth.authenticate(username=username, password=password)

            # проверяем не удален ли пользователь
            if user.is_active:
                # логинимся и делаем редирект на страницу home
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:index'))


# def login(request):
#     # проверяем какой запрос пришел
#     if request.method == 'POST':
#         # передаем в переменную пришедшие данные
#         form = UserLoginForm(data=request.POST)
#         # проверяем правильно ли заполнены поля
#         if form.is_valid():
#             # получаем пароль и логин
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             # если данные действительны, возвращаем объект пользователя.
#             user = auth.authenticate(username=username, password=password)
#
#             # проверяем не удален ли пользователь
#             if user.is_active:
#                 # логинимся и делаем редирект на страницу home
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('mainapp:index'))
#     else:
#         form = UserLoginForm()
#     content = {
#         'title': 'Авторизация',
#         'form': form
#     }
#     return render(request, 'authapp/login.html', content)

# class RegisterView(View):
#     def get(self, request):
#         form = UserRegisterForm()
#         content = {
#             'title': 'Регистрация',
#             'form': form
#         }
#         return render(request, 'authapp/register.html', content)
#
#     def post(self, request):
#         form = UserRegisterForm(data=request.POST)
#         # проверяем правильно ли заполнены поля
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно зарегистрирован')
#             return HttpResponseRedirect(reverse('authapp:login'))

def register(request):
    # проверяем какой запрос пришел
    if request.method == 'POST':
        # передаем в переменную пришедшие данные
        form = UserRegisterForm(data=request.POST)
        # проверяем правильно ли заполнены поля
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()
    content = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', content)


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return render(request, 'mainapp/index.html')


# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')

class ProfileView(CustomLoginDispatchMixin, View):
    def get(self, request):
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

        user_select = request.user

        # baskets = Basket.objects.filter(user=user_select)

        content = {
            'title': 'eShopper | Profile',
            'form': UserProfileForm(instance=request.user),
            'basket': Basket.objects.filter(user=user_select)
        }
        return render(request, 'authapp/profile.html', content)


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#     user_select = request.user
#
#     baskets = Basket.objects.filter(user=user_select)
#
#     content = {
#         'title': 'eShopper | Profile',
#         'form': UserProfileForm(instance=request.user),
#         'basket': Basket.objects.filter(user=user_select)
#     }
#     return render(request, 'authapp/profile.html', content)
