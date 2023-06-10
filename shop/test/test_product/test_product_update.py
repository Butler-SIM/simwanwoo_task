import json

from django.urls import reverse
from shop.test.test_product.test_product_read import ProductTestCase


class ProductUpdateTestCase(ProductTestCase):
    def test_product_update(self):
        """상품 수정 성공"""
        update_url = reverse("products-detail", kwargs={"pk": self.product.pk})
        self.client.force_authenticate()

        response = self.client.patch(
            update_url,
            json.dumps(
                {
                    "pk": self.product.pk,
                    "name": "TestProductUpdate",
                    "option_set": [
                        {
                            "pk": 1,
                            "name": "TestOption1",
                            "price": 1000,
                        },
                        {
                            "pk": 2,
                            "name": "Edit TestOption2",
                            "price": 1500,
                        },
                        {
                            "name": "Edit New Option",
                            "price": 300,
                        },
                    ],
                    "tag_set": [
                        {
                            "pk": 1,
                            "name": "ExistTag",
                        },
                        {
                            "pk": 7,
                            "name": "NewTag",
                        },
                        {
                            "name": "Edit New Tag",
                        },
                    ],
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.data.get("name"), "TestProductUpdate")
        self.assertEqual(response.status_code, 200)
        print("test_product_update : ", response.data)
