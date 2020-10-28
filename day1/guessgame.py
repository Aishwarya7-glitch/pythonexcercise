choice=8
print("Please guess a number between 1 and 15: ")
playerchoice = int(input())
if playerchoice > choice:
    print("The number is higher")
else:
    print("The number is lower")