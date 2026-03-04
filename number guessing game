import random
def main():
    print("\n")
    print("Number Guessing Game")
    print("____________________")
    print("choose an option")
    print("1.whole number")
    print("2.1 decimal place")
    print("3.2 decimal places")
    print("4.Exit")
    choice=int(input("Enter your choice "))

    if choice==1:
        num1=random.randint(1,100)
        num2=int(input("Enter a number from 1-100 "))
        while num1!=num2:
            if num1>num2:
                print("Too low. Try again")
            else:
                print("Too high. Try again")
            num2=int(input("Enter a number from 1-100 "))
        print("You're correct.")
        main()
    
    if choice==2:
        num1=round(random.uniform(1,100),1)
        num2=float(input("Enter a number from 1-100 "))
        while num1!=num2:
            if num1>num2:
                print("Too low. Try again")
            else:
                print("Too high. Try again")
            num2=float(input("Enter a number from 1-100 "))
        print("You're correct.")
        main()
    
    if choice==3:
        num1=round(random.uniform(1,100),2)
        num2=float(input("Enter a number from 1-100 "))
        while num1!=num2:
            if num1>num2:
                print("Too low. Try again")
            else:
                print("Too high. Try again")
            num2=float(input("Enter a number from 1-100 "))
        print("You're correct.")
        main()
    
    if choice==4:
        while True:
            break

main()






