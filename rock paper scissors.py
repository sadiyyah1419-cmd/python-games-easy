import random
list=["rock","paper","scissors"]
computer=random.choice(list)
user=input("Choose rock, paper or scissors")
if user=="rock" and computer=="rock" or user=="paper" and computer=="paper" or user=="scissors" and computer=="scissors":
    print("draw")
elif user=="rock" and computer=="paper" or user=="paper" and computer=="scissors" or user=="scissors" and computer=="rock":
    print("You loose")
elif computer=="rock" and user=="paper" or computer=="paper" and user=="scissors" or computer=="scissors" and user=="rock":
    print("You win")
else:
    print("Try again")