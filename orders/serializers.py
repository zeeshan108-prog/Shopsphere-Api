from rest_framework import serializers
from .models import Cart,CartItem,Order,OrderItem
from store.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source="product.name")

    class Meta:
        model=CartItem
        fields=['id','product','product_name','quantity']

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)

    class Meta:
        model=Cart
        fields=['id','user','items']
        read_only_fields=['user']


class OrderItemSerializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source='product.name')

    class Meta:
        model=OrderItem
        fields=['product','product_name','quantity','price_at_purchase']

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model=Order
        fields=['id','user','total_amount','status','items']
        read_only_fields=['user','total_amount']