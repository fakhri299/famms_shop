from django.urls import path
from . import views


urlpatterns = [
    path('',views.products,name='products'),
    path('<int:product_id>',views.product_detail,name='products-detail'),
    path('categories/<slug:category_slug>/',views.products,name='products-category'),
    
    
    
    
   
    
]




