from django.urls import path

from ecommerce.views import IndexView, ProductDetailView, ProductsView

app_name = 'ecommerce'

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('products', ProductsView.as_view(), name="products"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
]