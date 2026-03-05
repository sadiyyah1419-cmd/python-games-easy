import random
number=random.randint(1,100)
guess=input("Enter your guess ")
score=0
while guess!="q":
    if number%2==1 and guess=="odd" or number%2==0 and guess=="even":
        score+=1
        print(f"You're correct. The number is {number}. Your score is {score}")
    elif number%2==0 and guess=="odd":
        print(f"It was even. The number is {number}. Your score is {score}")
    elif number%2==1 and guess=="even":
        print(f"It was odd. The number is {number}. Your score is {score}")
    else:
        print("Try again")
    number=random.randint(1,100)
    guess=input("Enter your guess ")

if guess=="q":
    print(f"Your score is {score}")
    while True:
        break
    