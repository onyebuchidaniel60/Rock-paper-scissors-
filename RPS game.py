import random
userinput= input("Rock,paper, or scissors?")

game=["Rock","paper","scissors"]
try:
    if userinput==game[0]:
        print("Rock")
        computer=random.choice(game)
        print(computer)
    elif userinput==game[1]:
        print("paper")
        computer=random.choice(game)
        print(computer)
    elif userinput==game[2]:
        print("scissors")
        computer=random.choice(game)
        print(computer)
except:
    raise valuerror

if userinput==computer:
    print("we have a draw")
else:
    if userinput==game[0] and computer==game[1]:
        print("you lost")
    elif userinput==game[0] and computer==game[2]:
        print("you won")
    elif userinput==game[1] and computer==game[0]:
        print("you won")
    elif userinput==game[1] and computer==game[2]:
        print("you lost")
    elif userinput==game[2] and computer==game[0]:
        print("you lost")
    elif userinput==game[2] and computer==game[1]:
        print("you won")
