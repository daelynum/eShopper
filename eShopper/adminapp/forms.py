from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from authapp.models import User


class UserAdminRegisterForm(UserCreationForm):
    class Meta:
        # модель для формы
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фото'
        self.fields['age'].widget.attrs['placeholder'] = 'Укажите возраст'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class AdminUserProfileForm(UserChangeForm):

    class Meta:
        # модель для формы
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(AdminUserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'