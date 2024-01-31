# Collecting Names Using lists
name = "pass"
name_list = []
while name != "":
    name = input(">>> Enter you're Name &  >>> For save press (ENTER) bottom : ")
    if name == "":
        break
    else:
        name_list.append(name)
        
print(">>> Members Name : ",name_list)
