# guess game
import random
chances = 0
comp = random.randint(1,101)
while(chances < 7):
    player_g = int(input("Enter your guess : "))
    chances += 1
    if(comp == player_g):
        print("***congrats YOU Won***")
        print("Number of guesses : ", chances)
        break
    elif(comp > player_g):
        print("Too low")
    elif(comp < player_g):
        print("Too high")
if chances == 7:
    print("You Lose!")