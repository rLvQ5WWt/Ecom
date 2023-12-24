from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CartView, CartItemView, ShippingInfoView, TransactionView

urlpatterns = [
    path('carts/', CartView.as_view(), name='cart'),
    path('cart-items/', CartItemView.as_view(), name='cart-item'),
    path('shipping-info/', ShippingInfoView.as_view(), name='shipping-info'),
    path('transactions/', TransactionView.as_view(), name='transaction'),
]

urlpatterns = format_suffix_patterns(urlpatterns)