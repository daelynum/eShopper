from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, FormView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from authapp.models import User
from mainapp.mixin import  BaseClassContextMixin


class LoginCustomView(LoginView, BaseClassContextMixin):
    title = 'Авторизация'
    form_class = UserLoginForm
    template_name = 'authapp/login.html'


# class LoginView(View):
#     def get(self, request):
#
#         form = UserLoginForm()
#         content = {
#             'title': 'Авторизация',
#             'form': form
#         }
#         return render(request, 'authapp/login.html', content)
#
#     def post(self, request):
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
class RegisterView(FormView, BaseClassContextMixin):
    title = 'Admin | Регистрация'
    form_class = UserRegisterForm
    model = User
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрировались \n '
                                          'На почту отправлено письмо для завершения регистрации')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылки'
        message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        user = User.objects.get(email=email)
        if user and user.activation_key == activate_key and not user.is_activation_key_expires():
            user.activation_key = ''
            user.activation_key_expires = None
            user.is_active = True
            user.save()
            auth.login(self, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(self, template_name='authapp/verification.html')
        else:
            return HttpResponseRedirect('authapp:index')


#
# def register(request):
#     # проверяем какой запрос пришел
#     if request.method == 'POST':
#         # передаем в переменную пришедшие данные
#         form = UserRegisterForm(data=request.POST)
#         # проверяем правильно ли заполнены поля
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно зарегистрирован')
#             return HttpResponseRedirect(reverse('authapp:login'))
#     else:
#         form = UserRegisterForm()
#     content = {
#         'title': 'Регистрация',
#         'form': form
#     }
#     return render(request, 'authapp/register.html', content)

class LogoutCustomView(LogoutView):
    template_name = 'mainapp/index.html'


# class LogoutView(View):
#     def get(self, request):
#         auth.logout(request)
#         return render(request, 'mainapp/index.html')


# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')

# class ProfileView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
#     # model = User
#     template_name = 'authapp/profile.html'
#     form_class = UserProfileForm
#     success_url = reverse_lazy('authapp:profile')
#     title = 'eShopper | Profile'
#
#     def get_object(self, queryset=None):
#         return User.objects.get(id = self.request.user.pk)

# class ProfileView(CustomLoginDispatchMixin, View):
#     def get(self, request):
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#
#         user_select = request.user
#
#         # baskets = Basket.objects.filter(user=user_select)
#
#         content = {
#             'title': 'eShopper | Profile',
#             'form': UserProfileForm(instance=request.user),
#             'basket': Basket.objects.filter(user=user_select)
#         }
#         return render(request, 'authapp/profile.html', content)

class ProfileFormView(UpdateView, BaseClassContextMixin):
    # model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    title = 'Gekshop | Профайл'

    def form_valid(self, form):
        messages.set_level(self.request,messages.SUCCESS)
        messages.success(self.request,'Вы успешно сохранили профиль')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileFormView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

    # def form_valid(self, form):
    #     messages.set_level(self.request, messages.SUCCESS)
    #     messages.success(self.request, 'Вы успешно сохранили профиль')
    #     super().form_valid(form)
    #     return HttpResponseRedirect(self.get_success_url())
    #
    # def get_object(self, queryset=None):
    #     return User.objects.get(id=self.request.user.pk)
    #
    # def post(self, request, *args, **kwargs):
    #     form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
    #     profile_form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.userprofile)
    #     if form.is_valid() and profile_form.is_valid():
    #         form.save()
    #     return redirect(self.success_url)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileFormView, self).get_context_data()
    #     # context['profile'] = UserProfileEditForm(instance=self.request.user.userprofile)
    #     return context
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
