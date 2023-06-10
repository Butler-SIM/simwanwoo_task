from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from shop.models import Product, ProductOption, Tag


class TagSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "pk",
            "name",
        ]


class ProductTagSerializer(WritableNestedModelSerializer):

    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = [
            "pk",
            "name",
        ]


class ProductOptionSerializer(WritableNestedModelSerializer):
    class Meta:
        model = ProductOption
        fields = [
            "pk",
            "name",
            "price",
        ]


class ProductSerializer(WritableNestedModelSerializer):
    option_set = ProductOptionSerializer(many=True)
    tag_set = ProductTagSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "pk",
            "name",
            "option_set",
            "tag_set",
        ]
