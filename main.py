import random

def quessthenumber():
    numbers = [1, 2 , 3, 4, 5]
    print("Welcome to Quess the Number")
    compnumber = random.choice(numbers)
    usernumber = int(input("What is your quess? Should not be more than 5. "))
    if compnumber == usernumber:
        print("You won!")
        print("The number was..." + str(compnumber))
    elif compnumber != usernumber:
        print("Bad luck...")
        print("The number was: " + str(compnumber))

quessthenumber()
    