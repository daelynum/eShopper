from django.urls import path

from adminapp.views import DeleteUserView, IndexTemplateView, UserListView, UserCreateView, UserUpdateView

app_name = 'adminapp'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', DeleteUserView.as_view(), name='user_delete'),
]