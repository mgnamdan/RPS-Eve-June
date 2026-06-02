# 1. Have computer make choice (X)
# 2. Have player make choice (X)
# 3. Determine winner
import random

compChoice = random.randint(1, 3)
# 1 -> rock
# 2 -> paper
# 3 -> scissors

print("")
print("Make a choice: (rock/paper/scissors)")
userChoice = input(" --> ").lower()

if userChoice == "rock":
    if compChoice == 1:
        print("You tie! You both chose rock!")
    elif compChoice == 2:
        print("You lose! The computer chose paper!")
    else:
        print("You win! The computer chose scissors!")
elif userChoice == "paper":
    if compChoice == 1:
        print("You win! The computer chose rock!")
    elif compChoice == 2:
        print("You tie! You both chose paper!")
    else:
        print("You lose! The computer chose scissors!")
elif userChoice == "scissors":
    if compChoice == 1:
        print("You lose! The computer chose rock!")
    elif compChoice == 2:
        print("You win! The computer chose paper!")
    else:
        print("You tie! You both chose scissors!")
else:
    print("That's not a real move!")
