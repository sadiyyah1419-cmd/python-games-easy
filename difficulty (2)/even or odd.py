import random
number=random.randint(1,100)
guess=input("Enter your guess ")
while guess!="q":
    if number%2==1 and guess=="odd" or number%2==0 and guess=="even":
        print("You're correct")
    elif number%2==0 and guess=="odd":
        print("It was even")
    elif number%2==1 and guess=="even":
        print("It was odd")
    else:
        print("Try again")
    number=random.randint(1,100)
    guess=input("Enter your guess ")

if guess=="q":
    while True:
        break
    