from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from authapp.views import login, register, logout, profile

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
