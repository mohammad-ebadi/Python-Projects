# Guess in rang(1-100)and count your guesses when you reach a specific number.
import random

x = 5
count=0
guess=0
while guess != x:
    guess=random.randint(1,10)
    print(guess)
    count = count + 1
print("Count : ",count)