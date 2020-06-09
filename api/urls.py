from django.urls import include, path

from rest_framework import routers

from ingredient.views import IngredientViewSet
from order.views import OrderViewSet
from order_item.views import OrderItemViewSet
from pizza.views import PizzaViewSet
from sauce.views import SauceViewSet

router = routers.DefaultRouter()
router.register(r'ingredient', IngredientViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order_item', OrderItemViewSet)
router.register(r'pizza', PizzaViewSet)
router.register(r'sauce', SauceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
