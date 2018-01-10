#Created by Scott Kim
#Lab1 Part 2

userInput = input("enter a sentense\n").split(" ")
newUserInput = [userInput[0].lower()] # put the first word into lowercase

del userInput[0] # delete the first word from the list

for word in userInput:
    titleWord = word[0].upper() + word[1:].lower() #Make the first letter of the word into uppercase and other letters into lowercase
    newUserInput.append(titleWord) #appends to the newUserInput
print(''.join(newUserInput))
