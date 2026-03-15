#-----------------SNAKE, WATER OR GUN GAME------------------

import random

def game(what):
    enter=["snake","water","gun"]
    computer=random.choice(enter)
    print(f"Computer Choice:{computer}")


    if(what == computer):
        print("It's a Draw!")

    elif(what == "snake" and computer == "water") or (what == "water" and computer == "gun") or (what == "gun" and computer == "snake"):
        print("You win!")
    
    elif what in enter:
        print("Computer win!")

    else:
        print("Invalid input!")



what=input("Enter snake, water or gun to play the game:").lower()
game(what)


#--------------------------------OR--------------------------------------
# computer= random.choice([-1,0,1])

# user=input("Enter your choice:")

# user_Dict={"snake":1, "water":0, "gun":-1}

# reverse_Dict={1:"snake", 0:"water", -1:"gun"}

# you = user_Dict[user]

# print(f"Your choice:{reverse_Dict[you]} \nComputer choice:{reverse_Dict[computer]}")

# if(computer == you):
#     print("It's a Draw!")

# elif(you==1 and computer==0) or (you==0 and computer==-1) or (you==-1 and computer==1): #OR if(computer - you % 3 == 1)
#     print("You win!")

# elif you in reverse_Dict:
#     print("Computer win!")

# else:
#     print("Invaild input!!!")
