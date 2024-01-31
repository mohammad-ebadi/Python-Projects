# Collecting Names Using lists
name = "pass"
name_list = []
count=0
while name != "":
    name = input(">>> Enter you're Name &  >>> For save press (ENTER) bottom : ")
    count=count+1
    if name == "":
        break
    else:
        name_list.append(name)
        
print(">>> Members Name and Count : ","(",count-1, ")",name_list)
