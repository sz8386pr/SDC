#Created by Scott Kim
#Lab1 Part 1

import random

rNumber = random.randrange(1, 10)

while True:
    uNumber = int(input("Guess the number between 1 to 10\n"))
    if uNumber == rNumber:
        print("You guessed it right!")
        break
    elif uNumber > rNumber:
        print("Your number is high")
    elif uNumber < rNumber:
        print("Your number is low")
