#Retail Billing with Multiple Discount Rules
amount = float(input("Enter purchase amount: "))
member = input("Are you a member? yes/no: ")

if amount >= 5000:
    discount = amount * 10 / 100
elif amount >= 2000:
    discount = amount * 5 / 100
else:
    discount = 0

if member == "yes":
    discount = discount + amount * 5 / 100

total = amount - discount

print("Purchase Amount:", amount)
print("Discount:", discount)
print("Final Amount:", total)
