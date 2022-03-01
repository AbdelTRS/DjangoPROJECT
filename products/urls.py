from django.urls import path, re_path
from . import views

# namespace
app_name = 'products'

urlpatterns = [

    # Retrieve product list
    path('', views.product_list, name='product_list'),

    # Retrieve single product object
    path('<id>', views.product_detail, name='product_detail'),

    # Update a product
    path('update/<id>', views.product_update, name='quantity')
]