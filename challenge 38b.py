#number
numbers=[]

#read a file from challenge 38
with open("numbers.txt", "r") as b:
    for line in b:
        number=int(line.strip())
        numbers.append(number)

#sum up the total and average numbers
total=sum(numbers)
average= total/ len(numbers)

#print the total and the average number of between 1 and 6
print("The total is " ,total, " and the average is " ,average)