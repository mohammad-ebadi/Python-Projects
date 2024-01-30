# Counting the characters in a string using a For loop
name=input("Enter you're first name :".strip())
count=0

for i in name :
    print("(",i.upper(),")")
    count=count+1
print(">>> ",count , "Character exist")
