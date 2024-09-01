from datetime import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  
    category_name = models.CharField(max_length=255)  

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    prod_name = models.CharField(max_length=50)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.prod_name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, null=False)  
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Order {self.order_id} for {self.customer_id}"
    
    
class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True) 
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE) 
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE) 
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)  
    amount = models.IntegerField()  

    def __str__(self):
        return f"OrderDetail {self.order_detail_id} - Product {self.product_id} for Order {self.order_id}"