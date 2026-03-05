import random
coin=["heads","tails"]
computer=random.choice(coin)
user=input("Enter heads or tails ")
while user!="q":
    if user==computer:
        print("You're correct.")
    elif user=="heads" and computer=="tails":
        print("It was tails")
    elif user=="tails" and computer=="heads":
        print("It was heads")
    else:
        print("Try again")
    computer=random.choice(coin)
    user=input("Enter heads or tails (Enter q to exit) ")

while True:
    if user=="q":
        break