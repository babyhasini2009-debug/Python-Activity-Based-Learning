#Manufacturing Cost and Profitability Analysis
quantity = int(input("Enter quantity: "))
material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
selling = float(input("Enter selling price: "))

cost = (material + labour) * quantity
income = selling * quantity
profit = income - cost

print("Total Cost:", cost)
print("Total Income:", income)

if profit > 0:
    print("Profit:", profit)
elif profit < 0:
    print("Loss:", -profit)
else:
    print("No Profit No Loss")
