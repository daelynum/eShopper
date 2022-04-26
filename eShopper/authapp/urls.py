from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from authapp.views import LoginCustomView, RegisterView, LogoutCustomView, ProfileFormView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginCustomView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutCustomView.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    
    path('verify/<str:email>/<str:activate_key>/', RegisterView.verify, name='verify')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
