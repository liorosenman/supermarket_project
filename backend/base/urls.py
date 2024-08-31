from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CategoryViewSet, CustomerViewSet, OrderDetailViewSet, ProductViewSet
from base import views

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'order_details', OrderDetailViewSet)

urlpatterns = [
     path('', views.index),
     path('register/', views.register),
     path('del_customer/', views.del_customer),
     path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
