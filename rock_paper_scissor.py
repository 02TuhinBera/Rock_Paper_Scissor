# Rock Paper Scissor Game

import random

def game_win(comp, you):
    # If two values are equal, then it is a tie.!!!!!!!
    if comp == you:
        return None
    # Check for all possibilities when computer choose 's'
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    # Check for all possibilities when computer choose 'w'
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 'w':
            return True
    # Check for all possibilities when computer choose 'g'
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
        
# print("Comp's Turn: Rock(r), Paper(p) or Scissor(s)?")          # You can take this line  or not 
rand_no=random.randint(1, 3)
if rand_no == 1:
    comp = 'r'
elif rand_no == 2:
    comp = 'p'
elif rand_no == 3:
    comp = 's' 

you = input("Your Turn: Rock(r), Paper(p) or Scissor(s): ")
a=game_win(comp, you)
print(f"Computer choose {comp}")           
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You win!")
else:
    print("You lose!")           