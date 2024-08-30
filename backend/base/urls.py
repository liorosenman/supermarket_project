from django.contrib import admin
from django.urls import include, path

from base import views

urlpatterns = [
     path('', views.index),
     path('register/', views.register),
     path('del_customer/', views.del_customer),
     path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
