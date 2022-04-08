from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from authapp.views import login, register, logout, profile
from basketapp.views import basket_add, basket_remove, basket_edit

app_name = 'basketapp'
urlpatterns = [
    path('add/<int:id>', basket_add, name='basket_add'),
    path('remove/<int:basket_id>', basket_remove, name='basket_remove'),
    path('edit/<int:id_basket>/<int:quantity>/', basket_edit, name='basket_edit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)