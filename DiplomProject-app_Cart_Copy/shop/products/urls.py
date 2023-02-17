from django.urls import path, re_path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('products/', views.products, name='products'),
#     path('products/<int:category_id>/', views.products, name='category'),
#     path('products/<int:page>', views.products, name='page'),
#     path('basket-add/<int:product_id>', views.basket_add, name="basket_add"),
#     path('products/basket-delete/<int:id>', views.basket_delete, name="basket_delete"),
#     path('post/<slug:product_slug>/', views.DetailProduct.as_view(), name='product'),
# ]

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    # path('products/', views.products, name='products'),
    # path('products/<int:category_id>/', views.products, name='category'),
    re_path(r'^products/$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list,
            name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail,
            name='product_detail'),
]
