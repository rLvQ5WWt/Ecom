from rest_framework import serializers

from .models import (
    Brand,
    Category,
    Product,
    ProductLine,
    ProductImage,
    Attribute,
    AttributeValue,
)


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = ["category_name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)


class ProductImageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id", "productline")


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ("name",)


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)

    class Meta:
        model = AttributeValue
        fields = ("attribute", "attribute_value")


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerialzer(many=True)
    attribute_value = AttributeValueSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = (
            "price",
            "sku",
            "quantity",
            "order",
            "product_image",
            "attribute_value",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop("attribute_value")
        attr_values = {}
        for key in av_data:
            attr_values.update({key["attribute"]["id"]: key["attribute_value"]})
        data.update({"specification": attr_values})
        return data


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")
    brand_name = serializers.CharField(source="brand.name")
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
            "attribute_value",
        )
