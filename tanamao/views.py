from django.shortcuts import render
from store.models import Product 
from category.models import Category

def home(request, category=None):

  if category:
    products = Product.objects.all().filter(is_available=True, category=category)
  else:
    products = Product.objects.all().filter(is_available=True)
    
  context = {
    'products': products,
  }
  return render(request, 'home.html', context)
