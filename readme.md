# DataBase:
## Users - Inherited django table
Id (PK)
## Products
ProductID (PK)
CategoryID (FK)
Price
ProductName
## Cart
CartID (PK)
CustomerID (FK)
Date
## Categories
CategoryID (PK)
## Order_Details
OrderDetailID (PK)
CartID (FK)
CustomerID (FK)
ProductID (FK)
Amount

----------------------------------------------
# Pages:

## Login page:
Login with password and username.
Error message if needed.
Client is directed to "Start a new shopping" page.

## Register:
Register with username, password and email.
Proper message, the user stays in the page.