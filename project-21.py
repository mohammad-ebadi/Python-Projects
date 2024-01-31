# Collecting Names Using lists
names = "pass"
name_list = []
while names != "":
    name = input(">>> Enter you're Name & \n>>> For save press (ENTER) bottom : ")
    if name == "":
        break
    else:
        name_list.append(name)
        
print(">>> Members Name : ",name_list)

