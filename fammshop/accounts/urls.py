from django.urls import path
from. import views

urlpatterns = [
    path('register/', views.register ,name="register" ),
    path('login/', views.user_login ,name="login" ),
    path("logout/",views.user_logout,name="logout"),
    path("dashboard/",views.user_dashboard, name="dashboard"),
    path("buy_products/",views.buy_products, name="buy_products"),
    path("delete_products/",views.delete_products, name="delete_products"),
]