from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list, name="products"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("orders/", views.order_list, name="orders"),
]
