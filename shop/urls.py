from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/kitchen/$', views.kitchen, name='index'),
    url(r'^/sports/$', views.sports, name='index'),
    url(r'^/electronics/$', views.electronics, name='index'),
    url(r'^/clothing/$', views.clothing, name='index'),
    url(r'^/(?P<product_id>[0-9]+)$', views.detail, name='detail'),
]
