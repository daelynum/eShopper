from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from authapp.views import login, register, logout, profile
from basketapp.views import basket_add, basket_remove

app_name = 'basketapp'
urlpatterns = [
    path('add/<int:id>', basket_add, name='basket_add'),
    path('remove/<int:basket_id>', basket_remove, name='basket_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
