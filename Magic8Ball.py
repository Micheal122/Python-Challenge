#import random
answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")
print("Welcome to the Magic 8 Ball !")
question=input("Ask me for any advice and i'll help you out.")
print("shaking....\n"*4)
choice=(1,2,3)
if choice==1:
    answer=answer1 
elif choice==2:
    answer=answer2 
else:
    answer=answer3
print(answer)