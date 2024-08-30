from datetime import timezone
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=50)
    telNum = models.CharField(max_length=15)
    # is_admin = models.BooleanField()
 
    def __str__(self):
           return self.username
    
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
    
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)  
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Cart {self.cart_id} for {self.customer}"
    
    
class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True) 
    cart_id = models.ForeignKey('Cart', on_delete=models.CASCADE) 
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE) 
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)  
    amount = models.IntegerField()  

    def __str__(self):
        return f"OrderDetail {self.order_detail_id} - Product {self.product_id} for Cart {self.cart_id}"