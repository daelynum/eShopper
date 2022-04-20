from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# from authapp.views import login, register, logout, profile
from basketapp.views import BasketAddView, BasketRemoveView, BasketEditView

app_name = 'basketapp'
urlpatterns = [
    path('add/<int:id>', BasketAddView.as_view(), name='basket_add'),
    path('remove/<int:basket_id>', BasketRemoveView.as_view(), name='basket_remove'),
    path('edit/<int:id_basket>/<int:quantity>/', BasketEditView.as_view(), name='basket_edit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
