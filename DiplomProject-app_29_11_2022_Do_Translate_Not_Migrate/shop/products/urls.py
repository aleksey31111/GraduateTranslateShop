from django.urls import path, re_path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>/', views.products, name='category'),
    path('products/<int:page>', views.products, name='page'),

    re_path(r'^products/$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list,
            name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail,
            name='product_detail'),




]
