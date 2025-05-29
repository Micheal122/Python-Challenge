num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number"))
if num1>num2:
    print(num1,"is greater than",num2)
if num1<num2:
    print(num2,"is greater than",num1)
if num1==num2:
    print(num1,"is equal to",num2)
elif num1<num2:
        print(num2,"is greater than",num1)
else:
        print(num1,"is greater than",num2)

choice=input("Which team are you in")
if choice in ("K","B"):
print("We have a special offer of 10% off ferrets for students in B or K team")
choice=input("Which home group are you in")
if choice not in ("XB1","XB2","XB3","XB4","XK1","XK2","XK3","XK4"):
print("Sorry you have not made a valid choice")