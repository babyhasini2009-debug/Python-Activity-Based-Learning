#Campus Event Financial Planning
participants = int(input("Enter number of participants: "))
registration = float(input("Enter registration fee per person: "))
food = float(input("Enter food expenses: "))
decoration = float(input("Enter decoration expenses: "))
other = float(input("Enter other expenses: "))

income = participants * registration
expenses = food + decoration + other
balance = income - expenses

print("Total Income:", income)
print("Total Expenses:", expenses)

if balance > 0:
    print("Profit:", balance)
elif balance < 0:
    print("Loss:", balance)
else:
    print("No Profit No Loss")

