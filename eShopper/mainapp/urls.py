from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainapp.views import IndexTemplateView, ProductDetail, products

app_name = 'mainapp'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('products/', products, name='products'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('category/<int:id_category>/', products, name='category'),
    path('?page=<int:page>/', products, name='page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)