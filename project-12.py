# Average Number Calculator
count = 0
total = 0
number = int(input("Enter a number :"))

while number != -1:
    total = total + number
    count = count + 1
    number = int(input("Enter a number :"))
print(">>> Avg : ", total/count)

