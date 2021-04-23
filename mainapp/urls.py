from django.urls import path
from django.conf.urls import url
from .views import TestView, ProductDetailView

urlpatterns = [
    path("products/",view=TestView.as_view(),name="cats"),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]
