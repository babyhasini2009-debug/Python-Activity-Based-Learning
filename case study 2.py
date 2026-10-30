#Hospital Billing and Patient Classification
name = input("Enter patient name: ")
days = int(input("Enter number of days: "))
print("1. General Room")
print("2. Special Room")
print("3. ICU Room")
choice = int(input("Enter room choice: "))
if choice == 1:
    room_bill = days * 1000
elif choice == 2:
    room_bill = days * 2000
elif choice == 3:
    room_bill = days * 5000
else:
    room_bill = 0
doctor = float(input("Enter doctor charges: "))
medicine = float(input("Enter medicine charges: "))
total = room_bill + doctor + medicine
print("Patient Name:", name)
print("Total Bill:", total)
if total >= 20000:
    print("Category: High")
elif total >= 10000:
    print("Category: Medium")
else:
    print("Category: Low")