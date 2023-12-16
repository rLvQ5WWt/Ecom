from rest_framework import serializers

from .models import Cart, CartItem


# The CartItemSerializer class is a serializer for CartItem objects.
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        # The model that this serializer is for.
        model = CartItem
        # The fields from the model that should be included in the serialized representation.
        fields = ['id', 'product', 'quantity', 'total_price', 'saved_for_later']

# The CartSerializer class is a serializer for Cart objects.
class CartSerializer(serializers.ModelSerializer):
    # The items field is a nested serializer. It includes a serialized representation of each CartItem in the Cart.
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        # The model that this serializer is for.
        model = Cart
        # The fields from the model that should be included in the serialized representation.
        fields = ['id', 'user', 'created_at', 'items']
