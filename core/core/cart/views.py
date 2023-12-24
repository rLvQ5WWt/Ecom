from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .models import Cart, CartItem, ShippingInfo, Transaction, Order
from .serializers import CartItemSerializer, CartSerializer, ShippingInfoSerializer, TransactionSerializer

# The CartView class is a viewset for Cart objects.

class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_item = CartItem.objects.filter(cart__user=request.user)
        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        cart_item = CartItem.objects.filter(pk=pk, cart__user=request.user).first()
        if cart_item:
            serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({"error": "Cart item not found"}, status=status.HTTP_400_BAD_REQUEST)
class ShippingInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        shipping_info = ShippingInfo.objects.filter(user=request.user).first()
        serializer = ShippingInfoSerializer(shipping_info)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShippingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        shipping_info = ShippingInfo.objects.filter(user=request.user).first()
        serializer = ShippingInfoSerializer(shipping_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(order__user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    # Transactions are typically created automatically when an order is placed,
    # so we might not need a post method here.