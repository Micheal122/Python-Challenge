localshop=int(input("How much did you spend?"))
print(localshop)
if localshop>10:
    print("you get a $1 voucher")
elif localshop>20:
    print("you get a $3 voucher")
else:
    print("no promotion")