from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.cart, name = 'cart'),
    re_path(r'cart/delete_cart/(?P<product_id>\d+)/$',views.delete_cart, name="delete_cart"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)