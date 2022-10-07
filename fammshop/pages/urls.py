from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('testimonials',views.testimonial,name='testimonial'),
    path('about',views.about,name='about'),
    path('contact',views.ContactView.as_view(),name='contact'),
    path('search/',views.search,name='search'),
  
    
]
