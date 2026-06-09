# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random


def determineWinner(playerChoice, computerChoice):
    a = playerChoice
    b = computerChoice

    result = ((a - b + 1) % 3) - 1

    if result == 1:
        print("Congratulations, you beat the computer!")
    elif result == 0:
        print("Good try! You tied the computer!")
    else:
        print("Better luck next time! You lose!")




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True

    while appOn:
        compChoice = random.randint(0, 2)
        # 0 -> rock
        # 1 -> paper
        # 2 -> scissors

        validChoice = False
        while not validChoice:
            print("")
            print("Make a choice: (rock/paper/scissors)")
            userChoice = input(" --> ").lower()

            if userChoice in ["rock", "paper", "scissors"]:
                validChoice = True

        if userChoice == "rock":
            userChoice = 0
        elif userChoice == "paper":
            userChoice = 1
        elif userChoice == "scissors":
            userChoice = 2
        else:
            print("That's not a real move!")

        print(f"The computer chose {compChoice}")
        determineWinner(userChoice, compChoice)


        validChoiceTwo = False
        while not validChoiceTwo:
            print("")
            print("Would you like to play another game?")
            anotherGame = input(" --> ").lower()

            if anotherGame in ["no", "n", "quit", "exit"]:
                validChoiceTwo = True
                appOn = False
            if anotherGame in ["yes", "y", "sure"]:
                validChoiceTwo = True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()