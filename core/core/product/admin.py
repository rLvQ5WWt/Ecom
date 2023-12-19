from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import (
    Attribute, AttributeValue, Brand, Category, Product, ProductImage, ProductLine, ProductType, ProductTypeAttribute,
)

# Register your models here.


class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )

        if instance.pk:
            link = mark_safe('<a href="{url}">edit</a>'.format(url=url))
            return link
        else:
            return ""

class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue.product_line_attribute_value.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    inlines = [AttributeValueInline]


admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(
    ProductType,
)
