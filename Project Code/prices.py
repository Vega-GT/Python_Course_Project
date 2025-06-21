# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:25:26 2024

@author: mimsh
"""

count =0
total=0
name = input("Please enter your full name: ")
min_price = float(input("Please enter the minimum price: "))
price_list = [30.45, 72.11, 15.55, 31.16, 19.30, 22.00, 56.75, 91.40, 39.77]
#loop through prices
for price in price_list:
    total+=price
    if price > min_price:
        count+=1
        
#output "Hello",name,"the minimum price is ",min_price
print("Hello",name,"the minimum price is", min_price)
#output "There are ",count,"prices greater than the minimum price"
print("There are",count,"prices greater than the minimum price!")
#output "The total price is ",sum
print("The total price is",total)
