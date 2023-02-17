from django.urls import re_path
from .views import cart_detail, cart_add, cart_remove

# app_name = 'cart'

urlpatterns = [
    re_path(r'^$', cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]