from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('about/', views.about),
]