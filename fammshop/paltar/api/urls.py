from django.urls import path
from . import views as api_views


urlpatterns = [
    path('paltarlar',api_views.PaltarCreateApiView.as_view(),name='paltar-listesi'),
    path('paltarlar/<int:pk>',api_views.PaltarDetailApiView.as_view(),name='paltar-detay'),
    path('description/<int:description_pk>/add_paltar',api_views.PaltarCreateApiView.as_view(),name='add-paltar'),

    

    path('categories',api_views.CategoryListCreateApiView.as_view(),name='category-listesi'),
    path('categories/<slug:slug>',api_views.CategoryDetailApiView.as_view(),name='category-detay'),

    path('description',api_views.DescriptionCreateApiView.as_view(),name='description-listesi'),
    path('description/<int:pk>',api_views.DescriptionDetailApiView.as_view(),name='description-detay'),


    
]