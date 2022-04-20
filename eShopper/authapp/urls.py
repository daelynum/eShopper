from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from authapp.views import LoginView, register, LogoutView, ProfileView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
