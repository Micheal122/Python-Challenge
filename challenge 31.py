import random
#Lets play Rock,Paper,Scissors game.
#choose this three variables in order to play the game
enter=input("Pick either rock, paper, and scissor")
choice=("rock","paper","scissor")
player=random.choice(possible_actions)
print("You chose" ,(choice), "the computor chose" ,(player))
#use one of the answer
if enter=="rock":
    print("You pick rock")
if player=="rock":
    print("player pick rock")
if enter=="paper":
    print("You pick paper")
if player=="paper":
    print("player pick paper")
if enter=="scissor":
    print("You pick scissor")
if player=="scissor":
    print("player pick scissor")
#The game is invalid
if player not in choice:
    print("This is an invalid answer, please type again")
if enter=="rock" and player=="rock":
if enter=="paper" and player=="paper":
if enter=="scissor" and player=="scissor":
print("It's a draw")
    