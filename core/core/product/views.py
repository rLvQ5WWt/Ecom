from django.db import connection
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product, ProductLine
from .serializers import BrandSerializer, CategorySerializer, ProductLineSerializer, ProductSerializer


# Create your views here.
class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    # query set that shows only active products. (custom model manager)
    queryset = Product.objects.isactive()

    lookup_field = "slug"

    # search for products based on slugs(slugs should be given manually in dashboard)
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug).select_related("category", "brand"),  # removes n+2 error
            many=True,
        )
        return Response(serializer.data)

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)  # list all products in

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",
        url_name="all",
    )
    def list_product_by_category(self, request, category=None):
        serializer = BrandSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
