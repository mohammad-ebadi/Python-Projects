# Number Guessing Game (revers version)
import random
a = 1
b = 100
hads = random.randint(a , b)
print(hads)

user = input("Is it you're number?")

while user != "c" :
    if user == "b" :
        a = hads
    if user == "s" :
        b = hads
    hads = random.randint(a,b)
    print(hads)
    user = input("Is it you're number?")

print(">>> You're number is ", hads)
# s = means (My number is smaller) /// b = means (My number is bigger) /// c = means (correct)
