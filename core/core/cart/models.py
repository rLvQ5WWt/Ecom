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
