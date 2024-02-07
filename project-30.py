# Check Postal Code
def code(x):
    if len(x) == 15:
        if x.isdigit :
            return True
    return False

x=input("Enter you're postal code :")
print(code(x))
