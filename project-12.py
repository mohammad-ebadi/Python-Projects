# Average number calculator
count = 0
totall = 0
number = int(input("Enter a number :"))

while number != -1:
    totall = totall + number
    count = count + 1
    number = int(input("Enter a number :"))
print(">>> Avg : ", totall/count)
