import random
dice=[1,2,3,4,5,6]
user=input("How many dice do you want to roll? ")

sum=0
while user!="q":
    try:
        for x in range(int(user)):
            computer=random.choice(dice)
            print(f"{x+1}. {computer}")
            sum=sum+computer
        print(sum)
        user=input("How many dice do you want to roll? ")
    except ValueError:
        print("Try again")
        user=input("How many dice do you want to roll? ")

if user=="q":
    while True:
        break

