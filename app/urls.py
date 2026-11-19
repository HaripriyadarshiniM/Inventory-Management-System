from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product-list/', views.product_list, name='product-list'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('add-product/', views.add_product, name='product-add'),
    path('supplier-list/', views.supplier_list, name='supplier-list'),
    path('add-supplier/',views.add_supplier, name='supplier-add'),
    path('category-list/', views.category_list, name='category-list'),
]
