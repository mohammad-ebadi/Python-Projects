# Determining whether a string is symmetrical or not
char=list(input("Enter a string:"))
print(char)
char_2= char[::-1]
print(char_2)
if char == char_2:
    print(">>> You're string is symmetrical")
else:
    print(">>> It's not symmetrical")
