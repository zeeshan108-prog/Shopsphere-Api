from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.db import transaction
from .models import Cart, CartItem, Order, OrderItem
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from store.models import Product
from django.db.models import Sum, Count
from rest_framework.decorators import action
from accounts.permissions import IsAdminUserCustom


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def create(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)

        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({"message": "Item added to cart"})
    


class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if request.user.role == "ADMIN":
            orders = Order.objects.all().prefetch_related('items__product')
        else:
            orders = Order.objects.filter(user=request.user).prefetch_related('items__product')

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        order = Order.objects.get(id=pk)

        new_status = request.data.get("status")

        allowed_transitions = {
            "PENDING": ["PAID", "CANCELLED"],
            "PAID": ["SHIPPED"],
            "SHIPPED": ["DELIVERED"],
            "DELIVERED": [],
            "CANCELLED": [],
        }

        if new_status not in allowed_transitions[order.status]:
            return Response({"error": "Invalid status transition"}, status=400)

        order.status = new_status
        order.save()

        return Response({"message": "Order status updated"})




class ReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUserCustom]

    def list(self, request):
        total_sales = Order.objects.filter(status="DELIVERED").aggregate(
            total=Sum('total_amount')
        )['total'] or 0

        total_orders = Order.objects.count()

        top_products = OrderItem.objects.values('product__name').annotate(
            total_sold=Sum('quantity')
        ).order_by('-total_sold')[:5]

        return Response({
            "total_sales": total_sales,
            "total_orders": total_orders,
            "top_products": top_products,
        })
