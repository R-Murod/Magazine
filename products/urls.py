from django.conf import \
    settings  # подтягивается все настройка целиком чем from store import settings
from django.urls import path

from products.views import *

app_name = 'products'

urlpatterns = [
    # path('', products, name='index'),
    path('', ProductsListView.as_view(), name='index'),
    # path('category/<int:category_id>/', products, name='category'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    # path('page/<int:page_number>/', products, name='paginator'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
