from rest_framework import viewsets
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from accounts.permissions import IsAdminUserCustom
from accounts.models import User


class IsAdminUserCustom(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role=='ADMIN'
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_deleted=False).select_related('category')
    serializer_class = ProductSerializer
    filterset_fields = ['category', 'price']
    search_fields = ['name']
    ordering_fields = ['price']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUserCustom()]
        return [AllowAny()]