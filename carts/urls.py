from django.urls import path
from . import views

urlpatterns = [
  path('', views.cart, name='cart'),
  path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
  path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
  path('clear_cart_item/<int:product_id>/', views.clear_cart_item, name='clear_cart_item'),

]