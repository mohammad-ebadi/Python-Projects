#Number guessing game

import random

answer = random.randint(1,100)
print(">>>",answer,"<<<")
print("...........................................\n")

number = int(input("Please enter a number in range (1-100) :"))

while number != answer:
    if number > answer:
        print(">>> It's Smaller...")
        print("...........................................\n")

    else:
        print(">>> It's Bigger...")
        print("...........................................\n")


    number = int(input("Enter you're next number : ")) 

print(">>>  Javab is :",answer," <<<")
    

