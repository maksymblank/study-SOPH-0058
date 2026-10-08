import random
import datetime


def playGame(switchChoice):
    prizeDoor = random.randint(1, 3)
    firstPick = random.randint(1, 3)

    # host opens a door that is not the prize and not the first pick
    hostOpen = random.randint(1, 3)
    while hostOpen == prizeDoor or hostOpen == firstPick:
        hostOpen = random.randint(1, 3)

    if switchChoice == True:
        # switch to the door that is left
        finalPick = 1
        while finalPick == firstPick or finalPick == hostOpen:
            finalPick = finalPick + 1
    else:
        finalPick = firstPick

    if finalPick == prizeDoor:
        win = True
    else:
        win = False

    return win


# main program
number = 0
wins = 0
losses = 0

while number <= 0:
  # try/catch block to handle invalid input
  try:
    number = int(input("How many games do you want to play? "))
  except ValueError:
    print("Please type a number bigger than 0")

# ask if user wants to switch doors
switchAnswer = input("Do you want to switch doors? (y/n) ")
switchAnswer = switchAnswer.lower()
if switchAnswer == "y":
    switchChoice = True
else:
    switchChoice = False

# play games
while number > 0:
    win = playGame(switchChoice)
    if win == True:
        wins = wins + 1
    else:
        losses = losses + 1
    number = number - 1

winPercentage = wins / (wins + losses) * 100
lossPercentage = losses / (wins + losses) * 100

print("Wins:", wins)
print("Losses:", losses)
print("Win percentage:", winPercentage, "%")
print("Loss percentage:", lossPercentage, "%")

file = open("logs.txt", "a")
file.write(str(datetime.datetime.now()) + ", " + str(number) + ", " + str(switchChoice) + ", " + str(wins) + ", " + str(losses) + ", " + str(winPercentage) + ", " + str(lossPercentage) + "\n")
file.close()
