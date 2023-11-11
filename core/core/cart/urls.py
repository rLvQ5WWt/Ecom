# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CartItemView, CartView

# Create a router object.
router = DefaultRouter()
# Register the CartView with the router under the path 'carts'.
router.register(r'carts', CartView, basename='cart')
# Register the CartItemView with the router under the path 'cart-items'.
router.register(r'cart-items', CartItemView, basename='cart-item')

# Define the URL patterns for this app.
urlpatterns = [
    # Include the router's URLs.
    path('', include(router.urls)),
]

"""
This will generate the following URLs:

For Carts:
- List: GET /carts/
- Create: POST /carts/
- Retrieve: GET /carts/{id}/
- Update: PUT /carts/{id}/
- Partial Update: PATCH /carts/{id}/
- Delete: DELETE /carts/{id}/

For CartItems:
- List: GET /cart-items/
- Create: POST /cart-items/
- Retrieve: GET /cart-items/{id}/
- Update: PUT /cart-items/{id}/
- Partial Update: PATCH /cart-items/{id}/
- Delete: DELETE /cart-items/{id}/

Replace {id} with the ID of the Cart or CartItem you want to retrieve, update, or delete.
"""
