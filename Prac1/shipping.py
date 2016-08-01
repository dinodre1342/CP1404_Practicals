quantity = int(input("Please enter quantity of the item"))
shipping_cost = 0

while quantity > 0:
    shipping_cost += float(input("Enter shipping cost:"))
    quantity -= 1

if shipping_cost > 100:
    print (shipping_cost - (shipping_cost * 0.1))
else:
    print (shipping_cost)





