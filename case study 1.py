#Progressive Electricity Billing
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 150 + (units - 100) * 2.5
elif units <= 500:
    bill = 400 + (units - 200) * 4
else:
    bill = 1600 + (units - 500) * 6

print("Units Consumed:", units)
print("Total Bill:", bill)
