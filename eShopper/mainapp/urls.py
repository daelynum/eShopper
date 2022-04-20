from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainapp.views import IndexTemplateView, ProductDetail, ProductView

app_name = 'mainapp'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('products/', ProductView.as_view(), name='products'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('category/<int:id_category>/', ProductView.as_view(), name='category'),
    path('?page=<int:page>/', ProductView.as_view(), name='page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)