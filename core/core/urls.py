from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.product import views as product_views  # Alias for the product app views
# Alias for the services app views
from core.services import views as services_views

router = DefaultRouter()
# Use the alias for the product app views
router.register(r"category", product_views.CategoryView)
router.register(r"product", product_views.ProductView)
router.register(r"brand", product_views.BrandView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("services/", include("core.services.urls")),
    # Use the alias for the services app view
    path("", services_views.home, name="home"),
    path('cart/', include('core.cart.urls')),
]
