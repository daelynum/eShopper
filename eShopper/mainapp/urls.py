from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainapp.views import products, index

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)