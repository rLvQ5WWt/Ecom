from django.conf import settings
from django.db import models

from core.product.models import Product, ProductLine


# The Cart model represents a shopping cart. Each user has one cart.
class Cart(models.Model):
    # The user who owns this cart. When the user is deleted, their cart is also deleted.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # The date and time when this cart was created.
    created_at = models.DateTimeField(auto_now_add=True)

# The CartItem model represents an item in a shopping cart.
class CartItem(models.Model):
    # The cart that this item belongs to. An item can be in one cart at a time.
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, null=True, blank=True)

    # The product line that this item is for. An item is for one product line.
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, null=True)
    # The quantity of this item in the cart.
    quantity = models.PositiveIntegerField(default=1)
    # The total price of this item, calculated as quantity * product_line.price.
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Whether this item is saved for later.
    saved_for_later = models.BooleanField(default=False)

    # The save method is called when you save an object.
    def save(self, *args, **kwargs):
        # Calculate the total price of this item.
        self.total_price = self.quantity * self.product_line.price
        # Call the parent class's save method.
        super().save(*args, **kwargs)


# models.py


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

   

    def __str__(self):
        return f"Order {self.id} for {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calculate the total price of this order item.
        self.total_price = self.quantity * self.product_line.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product_line.product.name} in Order {self.order.id}"


class ShippingInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    method = models.CharField(max_length=255)

    def __str__(self):
        return f"Shipping Info for {self.user.username}"

class Transaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=50, default='Pending')  # Example: 'Pending', 'Paid', 'Failed', etc.
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} for Order {self.order.id}"