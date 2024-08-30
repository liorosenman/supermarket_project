from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from flask import Response
from .models import Customer, Product
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def index(req):
    return JsonResponse('hello', safe=False)

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
	return "I'm protected"

@api_view(['DELETE'])
def del_customer(request):
        admin_users = Customer.objects.filter(username='admin')
        admin_users.delete()
        return JsonResponse({"msg": "Admin users deleted successfully"})


