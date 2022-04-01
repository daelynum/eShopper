import django.contrib.auth.context_processors
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm


def login(request):
    # проверяем какой запрос пришел
    if request.method == 'POST':
        # передаем в переменную пришедшие данные
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
                return HttpResponseRedirect(reverse('home'))
            else:
                print('user не найден')
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    content = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', content)


def register(request):
    # проверяем какой запрос пришел
    if request.method == 'POST':
        # передаем в переменную пришедшие данные
        form = UserRegisterForm(data=request.POST)
        # проверяем правильно ли заполнены поля
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    content = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', content)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
