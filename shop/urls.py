from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/register/$', views.UserFormView.as_view(), name='register'),
    url(r'^/(?P<product_id>[0-9]+)$', views.detail, name='detail'),
]
