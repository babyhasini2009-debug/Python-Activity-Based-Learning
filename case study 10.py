#Password Policy Validation Engine

password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch >= 'A' and ch <= 'Z':
        upper = 1
    elif ch >= 'a' and ch <= 'z':
        lower = 1
    elif ch >= '0' and ch <= '9':
        digit = 1
    else:
        special = 1

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")
