# Income Calculator for a day (by using function)

def income():
    print("\n..........<<< Welcome >>>..........\n")
    x1=float(input(">>> Enter you're income (per_hour($)) : "))
    x2=float(input(">>> Enter number of working hours per day (h) : "))
    x3=x1*x2
    print(">>> You're income for each day is >>> ",x3,"$")
    print("\n..........<<< The End >>>..........\n")

income()