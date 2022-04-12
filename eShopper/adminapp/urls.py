from django.urls import path

from adminapp.views import admin_users, index, user_create, user_delete, user_update

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user_create/', user_create, name='user_create'),
    path('user_update/<int:id>/', user_update, name='user_update'),
    path('user_delete/<int:id>/', user_delete, name='user_delete'),
]