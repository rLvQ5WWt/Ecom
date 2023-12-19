from rest_framework import viewsets

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


# The CartView class is a viewset for Cart objects.
class CartView(viewsets.ModelViewSet):
    # The queryset that this viewset operates on.
    queryset = Cart.objects.all()
    # The serializer class used to serialize and deserialize Cart objects.
    serializer_class = CartSerializer

# The CartItemView class is a viewset for CartItem objects.
class CartItemView(viewsets.ModelViewSet):
    # The queryset that this viewset operates on.
    queryset = CartItem.objects.all()
    # The serializer class used to serialize and deserialize CartItem objects.
    serializer_class = CartItemSerializer

    # The perform_update method is called when an existing object is updated.
    def perform_update(self, serializer):
        # Get the object that is being updated.
        instance = self.get_object()
        # Update the quantity and saved_for_later fields of the object.
        instance.quantity = self.request.data.get('quantity', instance.quantity)
        instance.saved_for_later = self.request.data.get('saved_for_later', instance.saved_for_later)
        # Save the updated object.
        instance.save()
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.viewsets import ViewSet

class CheckoutView(ViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({'detail': 'No items in the cart'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            # Create an order
            order = Order.objects.create(
                user=request.user,
                total=cart.items.aggregate(total=models.Sum('total_price'))['total'] or 0
            )

            # Move items from cart to order
            for item in cart.items.all():
                item_data = {'product_line': item.product_line.id, 'quantity': item.quantity, 'total_price': item.total_price}
                item_serializer = OrderItemSerializer(data=item_data)
                if item_serializer.is_valid(raise_exception=True):
                    OrderItem.objects.create(order=order, **item_serializer.validated_data)

            # Clear the cart
            cart.items.all().delete()

        return Response({'detail': 'Checkout successful'}, status=status.HTTP_200_OK)