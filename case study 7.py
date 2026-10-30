#Attendance Recovery Computation
total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))
target = int(input("Enter targeted attendence percentage"))

current_percent=(attended/total)*100
print("Your current attendence is",current_percent)

if current_percent>=target:
    print("Perfect Attendence")
elif current_percent<target:
    print("More classes Required")
required_classes=((target*total)-(100*attended))/(100-target)
print("You need to attend",required_classes,"more classes")