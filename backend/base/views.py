from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from flask import Response
from .models import Cart, Category, Customer, OrderDetail, Product
from rest_framework.decorators import api_view, permission_classes
from .serializers import CartSerializer, CategorySerializer, CustomerSerializer, OrderDetailSerializer, ProductSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


def index(req):
    return JsonResponse('hello', safe=False)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer



@api_view(['POST'])
def register(request):
    customer = Customer.objects.create(
                username=request.data['username'],
                password=request.data['password'],
                address=request.data['address'],
                telNum=request.data['telNum']
            )
    customer.save()
    return JsonResponse({"msg":"New customer created"})

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, customer):
        token = super().get_token(customer)
        token['username'] = customer.username
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
# 	return Response({"msg" : "I am protected"})

@api_view(['DELETE'])
def del_customer(request):
        admin_users = Customer.objects.filter(customer_id=9)
        admin_users.delete()
        return JsonResponse({"msg": "Admin users deleted successfully"})


