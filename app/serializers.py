from rest_framework import serializers

from .models import Order, OrderItem, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "stocks",
        )

    # Field Level validation
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    product_name = serializers.CharField(source="Product.name")
    # without this it will display id but once you pass the product serializer
    # it will get the id relevent information will display

    class Meta:
        model = OrderItem
        fields = (
            "product_name",
            "quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Nested Serializer
    # items need to configure related name in model
    total_price = serializers.SerializerMethodField(method_name="total")

    # def get_total_price(self, obj):
    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model = Order
        fields = ("order_id", "created_at", "user", "status", "items", "total_price")
