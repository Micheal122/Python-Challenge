#number range from 1 to 6
number=(1,2,3,4,5,6)

#insert a number between 1 and 6
with open("number.txt", "w") as a:
    for numbers in number:
        a.write(str(numbers) + "\n")

#print the number you entered
print("You have picked:", number)
