from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.orderPage, name = 'orderpage'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)