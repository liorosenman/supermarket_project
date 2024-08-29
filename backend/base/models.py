from datetime import timezone
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True, max_length=50)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telNum = models.IntegerField(max_length=10)
    fields =['id','username', 'address', 'telNum']
 
    def __str__(self):
           return self.desc
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  
    category_name = models.CharField(max_length=255)  

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(max_length=50)
    prod_name = models.CharField(max_length=50)
    fields =['prod_id','category_id', 'price', 'prod_name']

    def __str__(self):
        return self.prod_name
    
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Cart {self.cart_id} for {self.customer}"
    
    
class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True) 
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE) 
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE) 
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  
    amount = models.IntegerField()  

    def __str__(self):
        return f"OrderDetail {self.order_detail_id} - Product {self.product_id} for Cart {self.cart_id}"