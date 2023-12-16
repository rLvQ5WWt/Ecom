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
