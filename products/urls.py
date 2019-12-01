from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    re_path(r'add_cart/(?P<product_id>\d+)/$',views.add_cart,name = "add_cart"),
    path('search',views.search,name="search"),
]
