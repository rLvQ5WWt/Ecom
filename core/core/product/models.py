from django.db import models
from django.db.models.query import QuerySet
from mptt.models import MPTTModel, TreeForeignKey


# custom model manager to filter all active products
class ActiveQuery(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
    )  # self relationship.(sub category)

    class MPPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(
        default=False
    )  # field to check if products are still active

    objects = ActiveQuery.as_manager()  # custom queryset reference

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="attribute_value"
    )

    def __str__(self):
        return f"{self.attribute}-{self.attribute_value}"


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=6)
    sku = models.CharField(max_length=100)
    quantity = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(blank=True)
    attribute_value = models.ManyToManyField(
        AttributeValue,
        through="ProductLineAttributeValue",
        related_name="product_line_attribute_value",
    )
    product_type = models.ForeignKey("ProductType", on_delete=models.CASCADE)
    objects = ActiveQuery.as_manager()

    def __str__(self):
        return str(self.order)


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE,
        related_name="product_attribute_value_av",
    )

    product_line = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name="product_attribute_value_pl"
    )

    class Meta:
        unique_together = ("attribute_value", "product_line")


class ProductImage(models.Model):
    alt_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default="test.jpg")
    productline = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name="product_image"
    )
    order = models.PositiveIntegerField(blank=True)

    def clean(self):
        qs = ProductImage.objects.filter(productline=self.productline)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("!Duplicate Value")

    def save(self):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    attribute = models.ManyToManyField(
        Attribute,
        through="ProductTypeAttribute",
        related_name="ProductTypeAttribute",
    )

    def __str__(self):
        return self.name


class ProductTypeAttribute(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="product_type_attribute_pt",
    )

    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="product_type_attribute_a"
    )

    class Meta:
        unique_together = ("attribute", "product_type")
