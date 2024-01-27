# Income Calculator for a (day/mounth/year) (by using function)

def income():
    print("\n..........<<< Welcome >>>..........\n")
    x1=float(input(">>> Enter you're income (per_hour($)) : "))
    x2=float(input(">>> Enter number of working hours per day (h) : "))
    x3=x1*x2
    x4=x3*15
    x5=x4*12
    print(">>> You're income for each day is >>> ",x3,"$")
    print(">>> You're income for each mounth is >>> ",x4,"$")
    print(">>> You're income for each year is >>> ",x5,"$")
    print("\n..........<<< The End >>>..........\n")

income()