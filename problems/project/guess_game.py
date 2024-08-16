import random
target = random.randint(1,100)
while  True:
    userchoice=input("Guess Target or Quit (Q) = ") 
    if (userchoice == "Q"):
        break
    #try:
        userchoice = int(userchoice)
    #except ValueError:
        print("Please enter a valid number or 'Q' to quit.")
        continue
    #userchoice ==int(userchoice)
    if (userchoice == target):
        print("Sucess")
        break
    elif (userchoice > target):
        print("Enter small number")
    else :
        print("Enter large number")
        
print("Game Overe ...")
        