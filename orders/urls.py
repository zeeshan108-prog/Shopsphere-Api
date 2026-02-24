from rest_framework.routers import DefaultRouter
from .views import CartViewSet, OrderViewSet,ReportViewSet

router = DefaultRouter()

router.register('cart', CartViewSet, basename='cart')
router.register('orders', OrderViewSet, basename='orders')
router.register('reports', ReportViewSet, basename='reports')

urlpatterns = router.urls