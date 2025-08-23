from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Product,Order,OrderItem
from app.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer

# from django.http import JsonResponse


# Create your views here.
# def product_list(request):
#     product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#     return JsonResponse({"data": serializer.data})


@api_view(["GET"])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, pk):
    # Step 1: Get the specific product from database
    product = get_object_or_404(Product, pk=pk)

    # Step 2: Pass the product object to serializer
    # This tells serializer: "Convert THIS product to JSON"
    serializer = ProductSerializer(product)

    # Step 3: serializer.data converts the product object to dictionary
    # Example output: {'id': 1, 'name': 'iPhone', 'price': 999.99}
    return Response(serializer.data)


@api_view(["GET"])
def order_list(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)
