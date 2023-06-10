import json
from django.urls import reverse
from shop.test.test_product.test_product_read import ProductTestCase


# Create your tests here.


class ProductCreateTestCase(ProductTestCase):
    product_create_url = reverse(
        "products-list",
    )

    def test_product_create(self):
        """상품 생성 성공"""
        self.client.force_authenticate()
        response = self.client.post(
            self.product_create_url,
            json.dumps(
                {
                    "name": "TestProduct",
                    "option_set": [
                        {
                            "name": "TestOption1",
                            "price": 1000,
                        },
                        {
                            "name": "TestOption2",
                            "price": 500,
                        },
                        {
                            "name": "TestOption3",
                            "price": 0,
                        },
                    ],
                    "tag_set": [
                        {
                            "pk": 1,
                            "name": "ExistTag",
                        },
                        {
                            "name": "NewTag",
                        },
                    ],
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.data["name"], "TestProduct")
        self.assertEqual(response.status_code, 201)
        print("test_product_create : ", response.data)
