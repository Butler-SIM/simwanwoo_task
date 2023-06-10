from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ProductViewSet, TagViewSet

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="products")
router.register(r"tag", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
