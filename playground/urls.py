from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('about/', views.about),
    path('products_detail/<int:my_id>/', views.product_detail),
    path('products_create', views.product_create),
]