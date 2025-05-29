#import random
import random

#show a list of students in which one of them will win
students=("Andrew" , "Bobby" , "Renato" ,  "Tracey", "Adam" ,  "Michael" , "Nicci" ,  "Mary" , "Lance" , "Soula")

#Automatically select a winner
win=random.choice(students)

print("Congratulations " ,win, ", you are awarded with a prize")


