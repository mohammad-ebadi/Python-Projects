# Sum of infinite numbers using functions
def sum(*numbers):
    
    total = 0
    
    for number in numbers:
        
        print(number)
        total = total + number
        
    return total

print(sum(1,2,3,4,5,6,7,8,9,10))
