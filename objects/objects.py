# Purpose: Understanding how to use Python objects and classes
from dataclasses import dataclass

# a class with three attributes
@dataclass # dataclass decorator automatically generates special methods like __init__, __repr__, etc.
class Product:
    name:str                # convert to str. Attribute 1
    price:float             # convert to float. Attribute 2
    discountPercent:int     # convert to int. Attribute 3

    # a get method that uses two attributes to perform a calculation
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # a get method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

# Description: This script imports the Product class from the objects module.
from objects import Product

# create two product objects
product1 = Product("Stanley 13 Ounce Hammer", 12.99, 62)
produc2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0)

# Print the product data
print("Product Data")
print(f"Name:              {product1.name}")
print(f"Price:             ${product1.price:.2f}")
print(f"Discount Percent:  {product1.discountPercent}%")
print(f"Discount Amount:   ${product1.getDiscountAmount():.2f}")
print(f"Discount Price:    ${product1.getDiscountPrice():.2f}")
