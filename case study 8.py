#Fuel Consumption and Route Comparison
r1 = float(input("Enter Route 1 distance: "))
r2 = float(input("Enter Route 2 distance: "))
mileage = float(input("Enter vehicle mileage: "))
price = float(input("Enter fuel price: "))

if mileage <= 0 or price < 0:
    print("Invalid details")
else:
    cost1 = (r1 / mileage) * price
    cost2 = (r2 / mileage) * price

print("Route 1 Cost:", cost1)
print("Route 2 Cost:", cost2)

if cost1 < cost2:
    print("Route 1 is cheaper")
elif cost2 < cost1:
    print("Route 2 is cheaper")
else:
    print("Both routes have equal cost")
