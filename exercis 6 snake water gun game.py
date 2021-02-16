# snake water gun game

import random
list1 = ["snake", "water", "gun"]
print("lets start the game")
attempts = 1
your_score = 0
computer_score = 0
for i in range(0,10):
    object1 = input("choose any one between snake water and gun\n")
    object2 = random.choice(list1)
    object2= object2.lower()
    print("opponent got", object2)
    print("you got", object1)

    if object1 == object2:
        print("this round got tie")

    elif object1 == "snake" and object2 == "water":
        print("you win this round")
        your_score +=1

    elif object1== "snake" and object2== "gun":
       print("you lost this round")
       computer_score +=1

    elif object1== "water" and object2 == "snake":
        print("you lost this round")
        computer_score += 1

    elif object1=="water" and object2=="gun":
         print("you win this round")
         your_score += 1

    elif object1=="gun" and object2=="snake":
        print("you win this round")
        your_score += 1

    elif object1 == "gun" and object2 == "water":
        print("you lost this round")
        computer_score += 1

    else:
        print(" ___invalid input___")

    attempts = attempts + 1
    print("you have", (11 - attempts), "more attempts")
    print("_____your score by now is_____", your_score)
    print("_____computer score by now is_____", computer_score)

print("\n")
print("your final score is", your_score)
print("computer's final score is", computer_score)
if your_score > computer_score:
    print("__________you won this match__________")

elif computer_score > your_score:
    print("__________you loose the match__________")

elif computer_score == your_score:
    print("__________match got tie__________")