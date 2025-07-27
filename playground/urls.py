from django.urls import path, reverse
from . import views

#URLconf
urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('about/', views.about),
    path('products/<int:my_id>/', views.product_detail,name="product_detail"),
    path('products_create', views.product_create),
    path('products/<int:my_id>/delete/', views.product_delete),
    path('product_list', views.product_list)
]