from django.urls import reverse
from rest_framework.test import (
    APITestCase,
)

from shop.models import Product, Tag


# Create your tests here.


class ProductTestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name="test_product")
        self.tag = Tag.objects.create(name="ExistTag")

    def tearDown(self):
        Product.objects.all().delete()
        Tag.objects.all().delete()


class ProductReadTestCase(ProductTestCase):
    def test_get_product_list(self):
        """상품 목록 조회 성공"""
        product_list_url = reverse(
            "products-list",
        )
        self.client.force_authenticate()
        response = self.client.get(product_list_url)
        self.assertEqual(response.status_code, 200)
        print("test_get_product_list : ", response.data)

    def test_get_product_detail(self):
        """상품 상세 조회 성공"""
        product_detail_url = reverse("products-detail", kwargs={"pk": self.product.pk})
        print("%%%%%%%%%%%%%%")
        print("product_detail_url : ", product_detail_url)
        self.client.force_authenticate()

        response = self.client.get(product_detail_url)

        self.assertEqual(response.data.get("pk"), 1)
        self.assertEqual(response.status_code, 200)
        print("test_get_product_detail : ", response.data)
